from typing import List, Tuple
from abc import ABC, abstractmethod
from proxy_enum.proxy_type import ProxyType


class Checker(ABC):
    def __init__(self, proxies: List[Tuple[ProxyType, List[str]]]) -> None:
        super().__init__()
        self._proxies = proxies
        self._filtered_proxies = []

    @property
    def proxies(self) -> List[Tuple[ProxyType, List[str]]]:
        return self._proxies

    @proxies.setter
    def proxies(self, value: List[Tuple[ProxyType, List[str]]]) -> None:
        self._proxies = value

    @property
    def filtered_proxies(self) -> List[str]:
        return self._filtered_proxies

    @filtered_proxies.setter
    def filtered_proxies(self, value: List[str]) -> None:
        self._filtered_proxies = value

    @abstractmethod
    def validate_http_proxy(self):
        pass

    @abstractmethod
    def validate_https_proxy(self):
        pass

    @abstractmethod
    def validate_socks4_proxy(self):
        pass

    @abstractmethod
    def validate_socks5_proxy(self):
        pass

    @abstractmethod
    def fetch_proxies(self) -> List[str]:
        pass
