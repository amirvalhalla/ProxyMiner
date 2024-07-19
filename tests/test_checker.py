import unittest
from typing import List, Tuple
from proxy_miner.proxy_enum.proxy_type import ProxyType
from proxy_miner.proxy_checker.checker import Checker


# Mock subclass of Checker to implement the abstract methods for testing
class MockChecker(Checker):
    def validate_http_proxy(self):
        pass

    def validate_https_proxy(self):
        pass

    def validate_socks4_proxy(self):
        pass

    def validate_socks5_proxy(self):
        pass

    def fetch_proxies(self) -> List[str]:
        return self.filtered_proxies


class TestChecker(unittest.TestCase):
    def setUp(self):
        # Initial setup for each test case
        self.proxies = [
            (ProxyType.HTTP, ["http://proxy1.com", "http://proxy2.com"]),
            (ProxyType.HTTPS, ["https://proxy3.com"]),
            (ProxyType.SOCKS4, ["socks4://proxy4.com"]),
            (ProxyType.SOCKS5, ["socks5://proxy5.com"]),
        ]
        self.checker = MockChecker(self.proxies)

    def test_proxies_property(self):
        self.assertEqual(self.checker.proxies, self.proxies)

    def test_proxies_setter(self):
        new_proxies = [
            (ProxyType.HTTP, ["http://newproxy1.com"]),
            (ProxyType.HTTPS, ["https://newproxy2.com"]),
        ]
        self.checker.proxies = new_proxies
        self.assertEqual(self.checker.proxies, new_proxies)

    def test_filtered_proxies_property(self):
        self.assertEqual(self.checker.filtered_proxies, [])

    def test_filtered_proxies_setter(self):
        new_filtered_proxies = ["http://filteredproxy1.com"]
        self.checker.filtered_proxies = new_filtered_proxies
        self.assertEqual(self.checker.filtered_proxies, new_filtered_proxies)

    def test_fetch_proxies(self):
        self.checker.filtered_proxies = ["http://proxy1.com", "https://proxy3.com"]
        self.assertEqual(
            self.checker.fetch_proxies(), ["http://proxy1.com", "https://proxy3.com"]
        )


if __name__ == "__main__":
    unittest.main()
