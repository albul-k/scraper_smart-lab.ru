
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from smartlab import settings
from smartlab.spiders.smartlab_dividend import SmartlabDividendSpider

if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(SmartlabDividendSpider)
    crawl_proc.start()
