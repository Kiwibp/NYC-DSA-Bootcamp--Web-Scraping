# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from craigslist_webscraping.items import CraigslistWebscrapingItem


class ProjectSpider(Spider):
    name = "craigsspider"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://asheville.craigslist.org/search/sss"]

    def parse(self, response):
        posts = response.xpath('//*[@id="sortable-results"]/ul/li').extract()
        for post in posts:
            name = Selector(text=post).xpath('//li/p/a/text()').extract()
            price = Selector(text=post).xpath('//li/p/span/span[@class="result-price"]/text()').extract()
            location = Selector(text=post).xpath('//li/p/span/span[@class="result-hood"]/text()').extract()
            date = Selector(text=post).xpath('//li/p/time/text()').extract()


            item = CraigslistWebscrapingItem()
            item['name'] = name
            item['price'] = price
            item['location'] = location
            item['date'] = date
            yield item

