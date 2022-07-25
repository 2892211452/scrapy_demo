import scrapy


class NewspiderSpider(scrapy.Spider):
    name = 'newspider'
    allowed_domains = ['test.com']
    start_urls = ['http://test.com/']

    def parse(self, response):
        pass
