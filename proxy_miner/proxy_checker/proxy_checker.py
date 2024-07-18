from proxy_enum.proxy_type import ProxyType
from .checker import Checker
from typing import List, Tuple
import requests
import socks
import socket


class ProxyChecker(Checker):
    def __init__(self, proxies: List[Tuple[ProxyType, List[str]]]) -> None:
        super().__init__(proxies)

    def validate_http_proxy(self, url: str):
        raise NotImplementedError

    def validate_https_proxy(self, url: str):
        raise NotImplementedError

    def validate_socks4_proxy(self, url: str):
        socks4_proxies = [proxy_url for proxy_type, proxy_urls in self.proxies if proxy_type ==
                          ProxyType.SOCKS4 for proxy_url in proxy_urls]

        for proxy in socks4_proxies:
            try:
                proxies = {
                    'http': f"socks4://{proxy}",
                    'https': f"socks4://{proxy}"
                }
                response = requests.get(
                    url, proxies=proxies, timeout=1, verify=False)
                if response.status_code == 200:
                    self.filtered_socks4_proxies.append(proxy)
                    response.close()
            except Exception as e:
                # TODO implement logger for the exception
                pass

    def validate_socks5_proxy(self, url: str):
        socks5_proxies = [proxy_url for proxy_type, proxy_urls in self.proxies if proxy_type ==
                          ProxyType.SOCKS5 for proxy_url in proxy_urls]

        for proxy in socks5_proxies:
            try:
                proxies = {
                    'http': f"socks5://{proxy}",
                    'https': f"socks5://{proxy}"
                }
                response = requests.get(
                    url, proxies=proxies, timeout=1, verify=False)
                if response.status_code == 200:
                    self.filtered_socks4_proxies.append(proxy)
                    response.close()
            except Exception as e:
                # TODO implement logger for the exception
                pass

    def validate_countries(self, countries: List[str]):
        raise NotImplementedError

    def validate_timeout(self, max_timeout: int):
        raise NotImplementedError

    def fetch_proxies(self) -> List[str]:
        return self.filtered_http_proxies + self.filtered_https_proxies + self.filtered_socks4_proxies + self.filtered_socks5_proxies
