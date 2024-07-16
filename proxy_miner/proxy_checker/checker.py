from typing import List, Tuple
from abc import ABC, abstractmethod
from proxy_enum.proxy_type import ProxyType


class Checker(ABC):
    def __init__(self, proxies: List[Tuple[ProxyType, List[str]]]) -> None:
        super().__init__()
        self._proxies = proxies
        self._filtered_http_proxies = []
        self._filtered_https_proxies = []
        self._filtered_socks4_proxies = []
        self._filtered_socks5_proxies = []

    @property
    def proxies(self) -> List[Tuple[ProxyType, List[str]]]:
        return self._proxies

    @proxies.setter
    def proxies(self, value: List[Tuple[ProxyType, List[str]]]) -> None:
        self._proxies = value

    @property
    def filtered_http_proxies(self) -> List[str]:
        return self._filtered_http_proxies

    @filtered_http_proxies.setter
    def filtered_http_proxies(self, value: List[str]) -> None:
        self._filtered_http_proxies = value

    @property
    def filtered_https_proxies(self) -> List[str]:
        return self._filtered_https_proxies

    @filtered_https_proxies.setter
    def filtered_https_proxies(self, value: List[str]) -> None:
        self._filtered_https_proxies = value

    @property
    def filtered_socks4_proxies(self) -> List[str]:
        return self._filtered_socks4_proxies

    @filtered_socks4_proxies.setter
    def filtered_socks4_proxies(self, value: List[str]) -> None:
        self._filtered_socks4_proxies = value

    @property
    def filtered_socks5_proxies(self) -> List[str]:
        return self._filtered_socks5_proxies

    @filtered_socks5_proxies.setter
    def filtered_socks5_proxies(self, value: List[str]) -> None:
        self._filtered_socks5_proxies = value

    @abstractmethod
    def validate_http_proxy(self, url: str):
        pass

    @abstractmethod
    def validate_https_proxy(self, url: str):
        pass

    @abstractmethod
    def validate_socks4_proxy(self, url: str):
        pass

    @abstractmethod
    def validate_socks5_proxy(self, url: str):
        pass

    @abstractmethod
    def validate_countries(self, countries: List[str]):
        pass

    @abstractmethod
    def validate_timeout(self, max_timeout: int):
        pass

    @abstractmethod
    def fetch_proxies(self) -> List[str]:
        pass
