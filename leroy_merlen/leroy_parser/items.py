# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


class LeroyParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field()
    cost = scrapy.Field()
    currency = scrapy.Field()
    unit = scrapy.Field()

    params_name = scrapy.Field()
    params_value = scrapy.Field()
    all_params = scrapy.Field()
    pass
