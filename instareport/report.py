"""Report target accounts."""
import os
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
    max_workers = min(32, (os.cpu_count() or 1) + 4)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(partial(report, proxies=proxies, targets=targets), range(max_workers))


def report(i, targets, proxies):
    while True:
        for account in targets:
            print("Reporting", account)
            attack.report_profile_attack(account, proxies.pop())


if __name__ == "__main__":
    main()
