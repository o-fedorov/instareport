"""Check the effectivenes of the approach."""
import ssl
from itertools import cycle
from pathlib import Path

from requests import Session
from requests.exceptions import ProxyError, SSLError

from instareport.vendor import proxy_harvester, user_agents

ROOT = Path(__file__).parent.parent
STUBS = ROOT / "stubs"
TEST = STUBS / "test.txt"
CHECK = STUBS / "check.txt"


def main():
    """Check the accounts to ensure they are allive."""
    proxies = iter(cycle(proxy_harvester.find_proxies()))

    test_statuses = 0
    check_statuses = 0

    for line in TEST.read_text().splitlines():
        test_statuses += check_is_alive(line, proxies)

    for line in CHECK.read_text().splitlines():
        check_statuses += check_is_alive(line, proxies)

    print("Test users:", test_status, "\nControl users:", check_statuses)


def check_is_alive(account, proxies):
    print("Checking", account)
    while True:
        try:
            return _check_is_alive(account, next(proxies))
        except (ssl.SSLError, ProxyError, SSLError):
            print("    Proxy error occured, retrying.")


def _check_is_alive(account, proxy):
    """Check if specific account is allive."""
    session = Session()

    session.proxies = {
        "https": f"https://{ proxy }",
        "http": f"https://{ proxy }",
    }

    resp = session.get(
        f"https://instagram.com/{ account }", 
        headers={"User-Agent": user_agents.get_user_agent()},
        timeout=10
    )
    if resp.status_code == 404:
        print("    The account is off.")
        return False
    if resp.status_code < 300:
        print("    The account is On.")
        return True

    resp.raise_for_status()


if __name__ == "__main__":
    main()
