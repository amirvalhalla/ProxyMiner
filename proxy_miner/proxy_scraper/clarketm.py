# pylint: disable=R0801

from typing import List, Tuple
import requests
from proxy_miner.proxy_enum.proxy_type import ProxyType
from .scraper import Scraper


class ClarketmScraper(Scraper):
    __timeout: float
    __proxy_url: str = (
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    )

    def __init__(self, timeout: float) -> None:
        super().__init__(
            [ProxyType.HTTP, ProxyType.HTTPS, ProxyType.SOCKS4, ProxyType.SOCKS5]
        )
        self.__timeout = timeout

    def scrape(self, proxy_type: ProxyType) -> List[Tuple[ProxyType, List[str]]]:
        proxies = self.__scrape(self.__proxy_url)

        result = [
            (ProxyType.HTTP, proxies),
            (ProxyType.HTTPS, proxies),
            (ProxyType.SOCKS4, proxies),
            (ProxyType.SOCKS5, proxies),
        ]

        return result

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
