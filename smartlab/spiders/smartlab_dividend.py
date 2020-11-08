import scrapy


class SmartlabDividendSpider(scrapy.Spider):
    name = 'smartlab_dividend'
    allowed_domains = ['smart-lab.ru']
    start_urls = ['https://smart-lab.ru/']

    def parse(self, response):
        pass
