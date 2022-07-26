import scrapy
from common import *

class SpiderDemo(scrapy.Spider):

    # 该蜘蛛爬虫的名字，运行时要用到
    name = "SpiderDemo"

    # 启动函数，爬虫从这里开始运行
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]


        # 传递参数给下一级
        for url in urls:
            yield scrapy.Request(url=url,meta={"a":"a"}, callback=self.parse)

        # # 多级页面爬虫
        # yield scrapy.Request(url='https://www.baidu.com', callback=self.first_parse)

    # 对爬取的结果进行解析的函数，回调函数
    def parse(self, response):
        print_green("para meta is ",response.meta)
        page = response.url.split("/")[-2]
        filename = f'github-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


    # 一级解析函数
    def first_parse(self, response):
        next_url = response.url
        yield scrapy.Request(url='https://www.bing.com', callback=self.second_parse)

    # 二级解析函数
    def second_parse(self, response):
        print_green("second page",response.url)
