# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy import Request
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class SmartlabPipeline:

    def __init__(self) -> None:
        db_client = MongoClient()
        self.db = db_client['smartlab']

    def process_item(self, item, spider):
        collection = self.db[type(item).__name__]
        collection.insert_one(item)
        return item

        # adapter = ItemAdapter(item)
        # if adapter['id'] in self.ids_seen:
        #     raise DropItem(f"Duplicate item found: {item!r}")
        # else:
        #     self.ids_seen.add(adapter['id'])
        #     return item
