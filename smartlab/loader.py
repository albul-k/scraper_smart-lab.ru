from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import unicodedata

from .items import SmartlabDivItem


def get_as_list(itms):
    return itms


def get_as_joined_list(itms):
    return ''.join(itms).strip()


def unicode_normalize(itm):
    return unicodedata.normalize("NFKD", itm)


class SmartlabDivLoader(ItemLoader):
    default_item_class = SmartlabDivItem
    url = TakeFirst()
    name_in = MapCompose(unicode_normalize)
    name_out = TakeFirst()
    ticker_out = TakeFirst()
    buy_till_out = TakeFirst()  # date
    cut_off_date_out = TakeFirst()  # date
    year_out = TakeFirst()
    period_out = TakeFirst()
    divident_out = TakeFirst()
    price_out = TakeFirst()
    dividend_yield_out = TakeFirst()
