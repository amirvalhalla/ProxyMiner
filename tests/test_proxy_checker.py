import unittest
from unittest.mock import patch, MagicMock
import requests
from proxy_miner.proxy_checker.proxy_checker import ProxyChecker
from proxy_miner.proxy_enum.proxy_type import ProxyType


class TestProxyChecker(unittest.TestCase):

    @patch("proxy_miner.proxy_checker.proxy_checker.requests.get")
    def test_validate_http_proxy_success(self, mock_get):
        # Setup
        proxies = [
            (ProxyType.HTTP, ["http_proxy1", "http_proxy2"]),
            (ProxyType.HTTPS, ["https_proxy1"]),
        ]
        url = "http://example.com"
        timeout = 5.0
        ssl_verify = False
        checker = ProxyChecker(proxies, url, timeout, ssl_verify)

        # Mock response for successful request
        mock_response = MagicMock()

        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        checker.validate_http_proxy()

        # Assert
        self.assertIn("http_proxy1", checker.fetch_proxies())
        self.assertIn("http_proxy2", checker.fetch_proxies())
        self.assertNotIn("https_proxy1", checker.fetch_proxies())

    @patch("proxy_miner.proxy_checker.proxy_checker.requests.get")
    def test_validate_http_proxy_failure(self, mock_get):
        # Setup
        proxies = [
            (ProxyType.HTTP, ["http_proxy1"]),
        ]
        url = "http://example.com"
        timeout = 5.0
        ssl_verify = False
        checker = ProxyChecker(proxies, url, timeout, ssl_verify)

        # Mock response for failed request
        mock_get.side_effect = requests.exceptions.RequestException

        # Act
        checker.validate_http_proxy()

        # Assert
        self.assertNotIn("http_proxy1", checker.fetch_proxies())

    @patch("proxy_miner.proxy_checker.proxy_checker.requests.get")
    def test_validate_https_proxy_success(self, mock_get):
        # Setup
        proxies = [
            (ProxyType.HTTPS, ["https_proxy1"]),
        ]
        url = "https://example.com"
        timeout = 5.0
        ssl_verify = True
        checker = ProxyChecker(proxies, url, timeout, ssl_verify)

        # Mock response for successful request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        checker.validate_https_proxy()

        # Assert
        self.assertIn("https_proxy1", checker.fetch_proxies())

    @patch("proxy_miner.proxy_checker.proxy_checker.requests.get")
    def test_validate_socks4_proxy_success(self, mock_get):
        # Setup
        proxies = [
            (ProxyType.SOCKS4, ["socks4_proxy1"]),
        ]
        url = "http://example.com"
        timeout = 5.0
        ssl_verify = False
        checker = ProxyChecker(proxies, url, timeout, ssl_verify)

        # Mock response for successful request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        checker.validate_socks4_proxy()

        # Assert
        self.assertIn("socks4_proxy1", checker.fetch_proxies())

    @patch("proxy_miner.proxy_checker.proxy_checker.requests.get")
    def test_validate_socks5_proxy_success(self, mock_get):
        # Setup
        proxies = [
            (ProxyType.SOCKS5, ["socks5_proxy1"]),
        ]
        url = "http://example.com"
        timeout = 5.0
        ssl_verify = False
        checker = ProxyChecker(proxies, url, timeout, ssl_verify)

        # Mock response for successful request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        checker.validate_socks5_proxy()

        # Assert
        self.assertIn("socks5_proxy1", checker.fetch_proxies())


if __name__ == "__main__":
    unittest.main()
