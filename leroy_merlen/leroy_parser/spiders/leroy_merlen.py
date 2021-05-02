import scrapy
from scrapy.http import HtmlResponse
from leroy_merlen.leroy_parser.items import LeroyParserItem


class LeroyMerlenSpider(scrapy.Spider):
    name = 'leroy_merlen'
    allowed_domains = ['naberezhnye-chelny.leroymerlin.ru']
    # start_urls = ['https://naberezhnye-chelny.leroymerlin.ru']

    def __init__(self, answer):
        super().__init__()
        url = f'https://naberezhnye-chelny.leroymerlin.ru/search/?q={answer}'
        # url = 'https://naberezhnye-chelny.leroymerlin.ru/search/?q=%D1%80%D0%B0%D0%B4%D0%B8%D0%B0%D1%82%D0%BE%D1%80'
        self.start_urls = [url]


    def parse(self, response):
        print(self.start_urls)
        pass