# from scrapy.crawler import CrawlerProcess
# from scrapy.settings import Settings

# from flask.smartlab import settings
# from flask.smartlab.spiders.smartlab_dividend import SmartlabDividendSpider

# if __name__ == '__main__':
#     crawl_settings = Settings()
#     crawl_settings.setmodule(settings)
#     crawl_proc = CrawlerProcess(settings=crawl_settings)
#     crawl_proc.crawl(SmartlabDividendSpider)
#     crawl_proc.start()

from app import app

if __name__ == "__main__":
    app.run()