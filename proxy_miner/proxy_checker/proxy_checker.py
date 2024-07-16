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
                          ProxyType.SOCKS5 for proxy_url in proxy_urls]

        for proxy in socks4_proxies:
            with requests.session() as session:
                try:
                    response = session.get(url, proxies={
                                           "http": f"socks4://{proxy}", "https": f"socks4://{proxy}"}, timeout=20)

                    if response.status_code == 200:
                        print(f"proxy: {proxy} worked response: {
                              response.content}")
                        self.filtered_socks4_proxies.append(proxy)
                    else:
                        print(f"proxy returned status code: {
                            response.status_code}")
                except Exception as e:
                    print(f"the proxy: {proxy} doesn't work error: {e}")

    def validate_socks5_proxy(self, url: str):
        raise NotImplementedError

    def validate_countries(self, countries: List[str]):
        raise NotImplementedError

    def validate_timeout(self, max_timeout: int):
        raise NotImplementedError

    def fetch_proxies(self) -> List[str]:
        return self.filtered_http_proxies + self.filtered_https_proxies + self.filtered_socks4_proxies + self.filtered_socks5_proxies
