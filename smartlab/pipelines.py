# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .bot.main import MyTelegramBot
from pymongo import MongoClient
from datetime import datetime


class SmartlabPipeline:

    def __init__(self) -> None:
        db_client = MongoClient()
        self.db = db_client['smartlab']
        self.collection = self.db['divident_calendar']
        self.collection.drop()

    def process_item(self, item, spider):

        buy_till: datetime = item.get('buy_till')
        if buy_till is not None and buy_till >= datetime.today():
            self.collection.insert_one(item)

        return item

    def close_spider(self, spider):

        docs: object = self.collection.find().sort('buy_till', 1)
        template: dict = {
            'buy_till': lambda x: x.strftime('%d.%m.%Y'),
            'cut_off_date': lambda x: x.strftime('%d.%m.%Y'),
            'ticker': lambda x: x,
            'name': lambda x: x,
        }

        table_data: str = ''

        for doc in docs:
            for key, value in template.items():
                table_data += value(doc[key]) + ', '
            table_data += '\n'

        bot = MyTelegramBot(
            chat_id='-418852529'
        )
        bot.send(table_data)
