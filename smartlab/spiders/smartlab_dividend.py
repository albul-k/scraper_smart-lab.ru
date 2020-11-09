import scrapy
# from ..items import SmartlabDivItem
from ..loader import SmartlabDivLoader


class SmartlabDividendSpider(scrapy.Spider):
    name = 'smartlab_dividend'
    allowed_domains = ['smart-lab.ru']
    start_urls = ['https://smart-lab.ru/dividends/']
    xpath = {
        'company': '//div[@class="container-calendar_table"]//table[contains(@class, "trades-table")]//a[@class="charticon2"]/@href',
    }

    def parse(self, response):
        for url in response.xpath(self.xpath['company']):
            yield response.follow(url, callback=self.company_parse)

    def company_parse(self, response):

        dividend_data = response.xpath(
            '//div[@class="wrapper__content"]//tr')[1].xpath('td')

        # Тикер
        # дата T-2
        # дата отсечки
        # Год
        # Период
        # дивиденд, руб
        # Цена акции
        # Див. доходность
        template = {
            'ticker': '',
            'buy_till': '',
            'cut_off_date': '',
            'year': '',
            'period': '',
            'divident': '',
            'price': '',
            'dividend_yield': '',
        }

        idx = 0
        data = {}
        for key, value in template.items():
            try:
                data[key] = dividend_data[idx].xpath('text()').get()
            except Exception:
                data[key] = None
            finally:
                idx += 1

        loader = SmartlabDivLoader(response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('name', '//div[@class="wrapper__content"]//h1/text()')
        loader.add_value('ticker', data['ticker'])
        loader.add_value('buy_till', data['buy_till'])
        loader.add_value('cut_off_date', data['cut_off_date'])
        loader.add_value('year', data['year'])
        loader.add_value('period', data['period'])
        loader.add_value('divident', data['divident'])
        loader.add_value('price', data['price'])
        loader.add_value('dividend_yield', data['dividend_yield'])
        yield loader.load_item()
