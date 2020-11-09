# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartlabDivItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    ticker = scrapy.Field()
    buy_till = scrapy.Field()
    cut_off_date = scrapy.Field()
    year = scrapy.Field()
    period = scrapy.Field()
    divident = scrapy.Field()
    price = scrapy.Field()
    dividend_yield = scrapy.Field()
