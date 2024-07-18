from proxy_scraper.speedx import SpeedXScraper
from proxy_enum.proxy_type import ProxyType
from proxy_checker.proxy_checker import ProxyChecker

if __name__ == "__main__":
    speedx_instance = SpeedXScraper()
    proxies_tuple = speedx_instance.scrape(ProxyType.ALL)

    with open('proxies.txt', 'w') as file:
        checker = ProxyChecker(
            proxies_tuple, "https://httpbin.org/ip", 1, False)
        checker.validate_socks5_proxy()
        for proxy in checker.fetch_proxies():
            file.write(proxy + "\n")
