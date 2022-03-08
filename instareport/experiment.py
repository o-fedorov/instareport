"""Check the effectiveness of the approach."""
import ssl
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

import requests
from instareport.proxy import ProxyPool
from instareport.vendor import user_agents
from requests.exceptions import RequestException

ROOT = Path(__file__).parent.parent
STUBS = ROOT / "stubs"
TEST = STUBS / "test.txt"
CHECK = STUBS / "check.txt"


def main():
    """Check the accounts to ensure they are alive."""
    proxies = ProxyPool()

    tasks = {}

    for line in TEST.read_text().splitlines():
        tasks[line] = "test"

    for line in CHECK.read_text().splitlines():
        tasks[line] = "check"

    with ThreadPoolExecutor() as executor:
        counts = Counter(
            zip(
                tasks.values(),
                executor.map(partial(check_is_alive, proxies=proxies), tasks),
            )
        )

    print(counts)


def check_is_alive(account, proxies):
    print("Checking", account)
    while True:
        proxy = proxies.pop()

        try:
            result = _check_is_alive(account, proxy)
        except (ssl.SSLError, RequestException) as err:
            print("    Request error occurred, retrying:", type(err))
        else:
            print("    Good proxy:", proxy),
            proxies.push(proxy)
            return result


def _check_is_alive(account, proxy):
    """Check if specific account is alive."""
    resp = requests.get(
        f"https://instagram.com/{ account }",
        headers={"User-Agent": user_agents.get_user_agent()},
        timeout=10,
        proxies = {"https": f"http://{ proxy }"}
    )
    if resp.status_code == 404:
        print("--->", account, ": the account is off.", "<---")
        return False
    if resp.status_code < 300:
        print("--->", account, ": the account is on.", "<---")
        return True

    resp.raise_for_status()


if __name__ == "__main__":
    main()
