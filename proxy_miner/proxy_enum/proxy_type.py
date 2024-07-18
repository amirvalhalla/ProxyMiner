# pylint: disable=too-few-public-methods
class ProxyType:
    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"
    ALL = [HTTP, HTTPS, SOCKS4, SOCKS5]
