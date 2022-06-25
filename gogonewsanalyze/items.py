# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GogonewsanalyzeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PostItem(scrapy.Item):

    id = scrapy.Field() 
    title = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()
    creationDate =  scrapy.Field()
    publishedDate =  scrapy.Field()
  