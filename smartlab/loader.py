from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import unicodedata
import re
from datetime import datetime
from typing import Optional

from .items import SmartlabDivItem


def get_as_list(itms):
    return itms


def get_as_joined_list(itms: list) -> str:
    return ''.join(itms).strip()


def unicode_normalize(itm: str) -> str:
    return unicodedata.normalize("NFKD", itm)


def get_year(itm: str) -> Optional[datetime]:
    try:
        itm: datetime = datetime.strptime(itm, '%Y')
    except ValueError:
        itm = None
    return itm


def get_date(itm: str) -> Optional[datetime]:
    try:
        itm: datetime = datetime.strptime(itm, '%d.%m.%Y')
    except ValueError:
        itm = None
    return itm


def get_num(itm: str) -> float:
    return float(itm.replace(',', '.'))


def get_divident(itm: str) -> str:
    regex: str = re.compile(r'.*[^\D]')
    return re.findall(regex, itm)


def get_name(itm: str) -> str:
    regex: str = re.compile(r'^Дивиденды\s+(.*):')
    return re.findall(regex, itm)


class SmartlabDivLoader(ItemLoader):
    default_item_class = SmartlabDivItem
    url = TakeFirst()

    name_in = MapCompose(unicode_normalize, get_name)
    name_out = TakeFirst()

    ticker_out = TakeFirst()

    buy_till_in = MapCompose(unicode_normalize, get_date)
    buy_till_out = TakeFirst()

    cut_off_date_in = MapCompose(unicode_normalize, get_date)
    cut_off_date_out = TakeFirst()

    year_in = MapCompose(unicode_normalize, get_year)
    year_out = TakeFirst()

    period_out = TakeFirst()

    divident_in = MapCompose(get_divident, get_num)
    divident_out = TakeFirst()

    price_in = MapCompose(get_num)
    price_out = TakeFirst()

    dividend_yield_in = MapCompose(get_divident, get_num)
    dividend_yield_out = TakeFirst()
