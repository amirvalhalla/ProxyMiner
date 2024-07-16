from abc import ABC, abstractmethod
from typing import List, Tuple
from proxy_enum.proxy_type import ProxyType


class Scraper(ABC):
    def __init__(self, supported_proxies: List[ProxyType]) -> None:
        super().__init__()
        self.supported_proxies = supported_proxies

    @property
    def supported_proxies(self) -> str:
        return self._supported_proxies

    @supported_proxies.setter
    def supported_proxies(self, value: List[ProxyType]) -> None:
        self._supported_proxies = value

    @abstractmethod
    def scrape(self, proxy_type: ProxyType) -> List[Tuple[ProxyType, List[str]]]:
        pass
