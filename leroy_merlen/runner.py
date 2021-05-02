from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leroy_parser import settings
from leroy_parser.spiders.leroy_merlen import LeroyMerlenSpider
# from book_labirint.spiders.labirint import LabirintSpider
# from book_labirint.spiders.book24 import Book24Spider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)

    answer = input('Что ищем: ')
    process.crawl(LeroyMerlenSpider, answer=answer)

    process.start()
