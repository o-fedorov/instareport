import re
from collections import deque
from threading import Lock

import requests
from instareport.vendor import user_agents


class ProxyPool:
    """Pool of HTTP proxies.

    Usage:
        import ssl
        from requests.exceptions import RequestException

        proxies = ProxyPool()
        proxy = proxies.pop()
        try:
            requests.get(..., proxies={"https": f"http://{ proxy }"})
        except (ssl.SSLError, RequestException):
            pass
        else:
            # The proxy is good, place it back.
            proxies.push(proxy)
    """
    def __init__(self, limit_proxies=50, watermark=60):
        self._watermark = watermark
        self._min_proxies = limit_proxies
        self._proxies = deque()
        self._proxy_candidates = deque()
        self._update_proxies_lock = Lock()

    def _sync(self):
        if len(self._proxies) + len(self._proxy_candidates) < self._watermark:
            proxies = self._fetch_proxy_candidates()

            with self._update_proxies_lock:
                known_proxies = set(self._proxies) | set(self._proxy_candidates)
                self._proxy_candidates.extend(self._proxies)
                self._proxy_candidates.extendleft(p for p in proxies if p not in known_proxies)


    def pop(self):
        with self._update_proxies_lock:
            if len(self._proxies) >= self._min_proxies:
                proxy = self._proxies.pop()
                self._proxies.appendleft(proxy)
                return proxy

        self._sync()
        return self._proxy_candidates.pop()

    def push(self, proxy):
        if proxy not in self._proxies:
            self._proxies.appendleft(proxy)

    def _fetch_proxy_candidates(self):
        resp = requests.get(
            "https://free-proxy-list.net/",
            headers={"User-Agent": user_agents.get_user_agent()},
        )
        return re.findall(r"(\d{1,3}(?:\.\d{1,3}){3}:\d+)", resp.text)
