# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class CraigslistWebscrapingItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
