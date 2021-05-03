# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


def create_dict(name,  list1):
    return dict(zip(name, list1))

def clear_text(txt):
    return txt.strip()
def to_float(txt):
    return float(txt)

class LeroyParserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    cost = scrapy.Field(input_processor=MapCompose(to_float))
    currency = scrapy.Field()
    unit = scrapy.Field()
    params_name = scrapy.Field()
    params_value = scrapy.Field(input_processor=MapCompose(clear_text))
    all_params = scrapy.Field()
