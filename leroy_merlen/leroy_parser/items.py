# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


def create_dict(name, list1):
    return dict(zip(name, list1))


def clear_text(txt):
    return txt.strip()


def to_float(txt: str):
    txt = txt.replace(' ', '')
    return float(txt)


def get_big_img(url: str):
    return url.replace('w_82,h_82', 'w_2000,h_2000')

class LeroyParserItem(scrapy.Item):
    _id = scrapy.Field()
    article = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(get_big_img))
    url = scrapy.Field(output_processor=TakeFirst())
    cost = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(to_float))
    currency = scrapy.Field(output_processor=TakeFirst())
    unit = scrapy.Field(output_processor=TakeFirst())
    params_name = scrapy.Field()
    params_value = scrapy.Field(input_processor=MapCompose(clear_text))
    all_params = scrapy.Field()
