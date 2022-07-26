import scrapy
from common import *

class NewspiderSpider(scrapy.Spider):
    name = 'newspider'
    # allowed_domains = ['test.com']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'testSpider.middlewares.ProcessAllExceptionMiddleware': 120,
        }
    }
    def start_requests(self):
        start_urls = [
            'https://api.github.com/repos/MeTitus/WServiceHost/commits?page=1&per_page=100',
            "https://www.baidu.com"
        ]

        yield scrapy.Request(url=start_urls[0], callback=self.parse)

    def parse(self, response):

        print_green("copy")
        pass
