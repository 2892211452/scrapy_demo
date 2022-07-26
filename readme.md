# scrapy爬虫demo


创建项目
```
scrapy startproject spider_demo
```

运行项目
```
scrapy crawl spider_demo
```

新增爬虫
```
 scrapy genspider newspider test.com   
```


# 中间件------异常处理文件
对应的是项目中的middlewares.py文件
然后在对应的爬虫里面配置好就行
