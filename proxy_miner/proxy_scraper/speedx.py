from proxy_enum.proxy_type import ProxyType
from .scraper import Scraper
import requests
from typing import List, Tuple


class SpeedXScraper(Scraper):
    socks4_url: str = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
    socks5_url: str = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"

    def __init__(self) -> None:
        super().__init__([ProxyType.SOCKS4, ProxyType.SOCKS5])

    def scrape(self, proxy_type: ProxyType) -> List[Tuple[ProxyType, List[str]]]:
        if proxy_type == ProxyType.ALL:
            socks4_proxies = self.__scrape_socks4()
            socks5_proxies = self.__scrape_socks5()

            result = [(ProxyType.SOCKS4, socks4_proxies),
                      (ProxyType.SOCKS5, socks5_proxies)]

            return result
        elif proxy_type == ProxyType.SOCKS4:
            socks4_proxies = self.__scrape_socks4()

            return [(ProxyType.SOCKS4, socks4_proxies)]
        elif proxy_type == ProxyType.SOCKS5:
            socks5_proxies = self.__scrape_socks5()

            return [(ProxyType.SOCKS5, socks5_proxies)]
        else:
            return []

    def __scrape_socks4(self) -> List[str]:
        with requests.get(self.socks4_url) as response:
            if response.status_code != 200:
                # TODO should implement logging instead of raising an error;
                # raise Exception(f"failed to retrieve data from {
                #                 self.socks4_url}, status code: {response.status_code}")
                return []

            response_content = response.text
            proxies = response_content.strip().splitlines()

            return proxies

    def __scrape_socks5(self) -> List[str]:
        with requests.get(self.socks5_url) as response:
            if response.status_code != 200:
                # TODO should implement logging instead of raising an error;
                # raise Exception(f"failed to retrieve data from {
                #                 self.socks4_url}, status code: {response.status_code}")
                return []

            response_content = response.text
            proxies = response_content.strip().splitlines()

            return proxies
