"""Report target accounts."""
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

from instareport.proxy import ProxyPool
from instareport.vendor import attack


ROOT = Path(__file__).parent.parent
STUBS = ROOT / "stubs"
TEST = STUBS / "test.txt"

def main():
    targets = TEST.read_text().splitlines()
    proxies = ProxyPool()

    with ThreadPoolExecutor() as executor:
        executor.map(partial(report, proxies=proxies), targets)


def report(account, proxies):
    print("Reporting", account)
    while True:
        attack.report_profile_attack(account, proxies.pop())


if __name__ == "__main__":
    main()
