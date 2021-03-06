import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroy_merlen.leroy_parser.items import LeroyParserItem


class LeroyMerlenSpider(scrapy.Spider):
    name = 'leroy_merlen'
    allowed_domains = ['naberezhnye-chelny.leroymerlin.ru']
    url_dom = ['https://naberezhnye-chelny.leroymerlin.ru']



    def __init__(self, answer):
        super().__init__()
        url = f'https://naberezhnye-chelny.leroymerlin.ru/search/?q={answer}'

        self.start_urls = [url]

    def parse(self, response: HtmlResponse):
        links = set(response.xpath('//div[contains(@class, "largeCard")]/a/@href').getall())

        for link in links:
            yield response.follow(self.url_dom[0] + link, callback=self.process_link)



    def process_link(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyParserItem(), response=response)
        loader.add_xpath("name", '//h1/text()')
        loader.add_xpath('photos', '//img[contains(@slot,"thumbs")]/@src')
        loader.add_value('url', response.url)
        loader.add_xpath('params_name', '//section[@id = "nav-characteristics"]//div//dt//text()')
        loader.add_xpath('params_value', '//section[@id = "nav-characteristics"]//div//dd//text()')
        loader.add_xpath('cost', '//span[@slot="price"]/text()')
        loader.add_xpath('currency', '//span[@slot="currency"]/text()')
        loader.add_xpath('unit', '//span[@slot="unit"]/text()')
        loader.add_value('article', response.url.split('-')[-1].replace('/', ''))

        # standart metod
        # name = response.xpath('//h1/text()').get()
        # url = response.url
        # #      rate = response.xpath('//div[@id="rate"]/text()').get()
        # #      authors = response.xpath('//div[@class="authors"]/a/text()').getall()
        # #      data_cost = response.xpath('//div[contains(@class, "buying-price")]/span/text()').getall()
        # params_name = response.xpath('//section[@id = "nav-characteristics"]//div//dt//text()').getall()
        # params_value = response.xpath('//section[@id = "nav-characteristics"]//div//dd//text()').getall()
        # photo_urls = response.xpath('//picture[@slot = "pictures"]//source/@data-origin')
        # item = LeroyParserItem()
        # item['name'] = name
        # item['url'] = url
        # item['params_name'] = params_name
        # item['params_value'] = params_value
        # print(1)
        # yield item
        yield loader.load_item()
