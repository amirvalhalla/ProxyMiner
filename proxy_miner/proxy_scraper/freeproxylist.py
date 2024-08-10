# pylint: disable=R0801

from typing import List, Tuple
import requests
import pycountry
from bs4 import BeautifulSoup
from proxy_miner.proxy_enum.proxy_type import ProxyType
from proxy_miner.validation.ip import is_valid_ip_port
from .scraper import Scraper


class FreeProxyList(Scraper):
    __proxy_url: str = "https://free-proxy-list.net"
    __timeout: float
    __filter_countries: List[str]

    def __init__(self, timeout: float, filter_countries: List[str]) -> None:
        super().__init__([ProxyType.HTTP, ProxyType.HTTPS])
        self.__timeout = timeout
        self.__filter_countries = filter_countries

    def scrape(self, proxy_type: ProxyType) -> List[Tuple[ProxyType, List[str]]]:
        if proxy_type not in self._supported_proxies and proxy_type != ProxyType.ALL:
            return []

        proxies = self.__scrape(self.__proxy_url)
        temp_proxies: List[str] = []

        for proxy in proxies:
            (proxy_addr_port, country_code) = self.__extract_proxy_detail(proxy)
            if (
                proxy_addr_port is None
                or country_code is None
                or not is_valid_ip_port(proxy_addr_port)
            ):
                continue

            if self.__filter_countries is not None and len(self.__filter_countries) > 0:
                country = pycountry.countries.get(alpha_2=country_code)
                if country is None or (
                    str(country.alpha_2) not in self.__filter_countries
                ):
                    continue

            temp_proxies.append(proxy_addr_port)

        proxies = temp_proxies

        if proxy_type == ProxyType.ALL:
            return [(ProxyType.HTTP, proxies), (ProxyType.HTTPS, proxies)]

        if proxy_type == ProxyType.HTTP:
            return [(ProxyType.HTTP, proxies)]

        if proxy_type == ProxyType.HTTPS:
            return [(ProxyType.HTTPS, proxies)]

        return []

    def __scrape(self, url: str) -> List[str]:
        try:
            response = requests.get(url, timeout=self.__timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            proxy_table = soup.find("table")
            rows = proxy_table.tbody.find_all("tr")

            proxies: List[str] = []
            for row in rows:
                columns = row.find_all("td")
                ip_address = columns[0].text
                port = columns[1].text
                country_code = columns[2].text
                merged: str = f"{ip_address}:{port} {country_code}"

                proxies.append(merged)
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
            return proxies
        finally:
            response.close()

    def __extract_proxy_detail(self, proxy: str) -> Tuple[str, str]:
        proxy_details = proxy.split(" ")
        if len(proxy_details) < 2:
            return (None, None)

        proxy_addr_port = proxy_details[0]
        country_code = proxy_details[1]

        return (proxy_addr_port, country_code)
