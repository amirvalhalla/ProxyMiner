# pylint: disable=R0801

from typing import List, Tuple
import requests
from proxy_miner.proxy_enum.proxy_type import ProxyType
from .scraper import Scraper


class SpeedXScraper(Scraper):
    __timeout: float
    __socks4_url: str = (
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
    )
    __socks5_url: str = (
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
    )

    def __init__(self, timeout: float) -> None:
        super().__init__([ProxyType.SOCKS4, ProxyType.SOCKS5])
        self.__timeout = timeout

    def scrape(self, proxy_type: ProxyType) -> List[Tuple[ProxyType, List[str]]]:
        if proxy_type not in self._supported_proxies and proxy_type != ProxyType.ALL:
            return []

        if proxy_type == ProxyType.ALL:
            socks4_proxies = self.__scrape_socks4()
            socks5_proxies = self.__scrape_socks5()

            result = [
                (ProxyType.SOCKS4, socks4_proxies),
                (ProxyType.SOCKS5, socks5_proxies),
            ]
            return result

        if proxy_type == ProxyType.SOCKS4:
            socks4_proxies = self.__scrape_socks4()
            return [(ProxyType.SOCKS4, socks4_proxies)]

        if proxy_type == ProxyType.SOCKS5:
            socks5_proxies = self.__scrape_socks5()
            return [(ProxyType.SOCKS5, socks5_proxies)]

        return []

    def __scrape_socks4(self) -> List[str]:
        return self.__scrape(self.__socks4_url)

    def __scrape_socks5(self) -> List[str]:
        return self.__scrape(self.__socks5_url)

    def __scrape(self, url: str) -> List[str]:
        try:
            response = requests.get(url, timeout=self.__timeout)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            return []
        except requests.exceptions.HTTPError:
            # TODO implement logger for the exception # pylint: disable=fixme
            return []
        except requests.exceptions.RequestException:
            # TODO implement logger for the exception # pylint: disable=fixme
            return []
        except Exception:  # pylint: disable=broad-exception-caught
            # TODO implement logger for the exception # pylint: disable=fixme
            return []
        else:
            response_content = response.text
            proxies = response_content.strip().splitlines()
            return proxies
        finally:
            response.close()
