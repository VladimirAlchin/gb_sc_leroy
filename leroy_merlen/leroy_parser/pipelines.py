# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.http import HtmlResponse
# pip install pillow

class LeroyParserPipeline:
    def __init__(self):
        self.client = MongoClient('localhost:27017')
        self.db = self.client['leroy']

    def process_item(self, item, spider):

        print(1)
        item['params_value'] = list(map(str.strip, item['params_value']))
        item['all_params'] = dict(zip(item['params_name'], item['params_value']))

        del item['params_name'], item['params_value']

        return item


from scrapy.pipelines.images import ImagesPipeline