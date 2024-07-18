from proxy_enum.proxy_type import ProxyType
from .checker import Checker
from typing import List, Tuple
import requests


class ProxyChecker(Checker):
    def __init__(self, proxies: List[Tuple[ProxyType, List[str]]], url: str, timeout: float, ssl_verify: bool) -> None:
        super().__init__(proxies)
        self.url = url
        self.timeout = timeout
        self.ssl_verify = ssl_verify

    def validate_http_proxy(self):
        self._validate(ProxyType.HTTP)

    def validate_https_proxy(self):
        self._validate(ProxyType.HTTPS)

    def validate_socks4_proxy(self):
        self._validate(ProxyType.SOCKS4)

    def validate_socks5_proxy(self):
        self._validate(ProxyType.SOCKS5)

    def fetch_proxies(self) -> List[str]:
        return self.filtered_proxies

    def _validate(self, pr_type: ProxyType):
        filtered_proxies = [proxy_url for proxy_type, proxy_urls in self.proxies if proxy_type ==
                            pr_type for proxy_url in proxy_urls]

        for proxy in filtered_proxies:
            try:
                proxies = {
                    'http': f"{str(pr_type).lower()}://{proxy}",
                    'https': f"{str(pr_type).lower()}://{proxy}"
                }
                response = requests.get(
                    self.url, proxies=proxies, timeout=self.timeout, verify=self.ssl_verify)
                if response.status_code == 200:
                    self.filtered_proxies.append(proxy)
                    response.close()
            except Exception as e:
                # TODO implement logger for the exception
                pass
