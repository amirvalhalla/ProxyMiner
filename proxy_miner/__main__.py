from proxy_miner.proxy_scraper.freeproxylist import FreeProxyList
from proxy_miner.proxy_enum.proxy_type import ProxyType
from proxy_miner.util.converter import Converter

if __name__ == "__main__":
    # speedx_instance = SpeedXScraper(10)
    # clarketm_instance = ClarketmScraper(10, ["US"])
    clarketm_instance = FreeProxyList(10, None)
    proxies_tuple = clarketm_instance.scrape(ProxyType.ALL)
    proxies = Converter.flatten_proxies(proxies_tuple)

    with open("proxies.txt", "w", encoding="utf-8") as file:
        # checker = ProxyChecker(proxies_tuple, "http://example.org", 1, False)
        # checker.validate_http_proxy()
        for proxy in proxies:
            file.write(proxy + "\n")
