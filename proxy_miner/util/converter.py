# pylint: disable=R0903

from typing import List, Tuple
from proxy_miner.proxy_enum.proxy_type import ProxyType


class Converter:
    @staticmethod
    def flatten_proxies(proxies_tuple: List[Tuple[ProxyType, List[str]]]) -> List[str]:
        flattened_list: List[str] = [
            ip for _, ip_list in proxies_tuple for ip in ip_list
        ]

        return flattened_list
