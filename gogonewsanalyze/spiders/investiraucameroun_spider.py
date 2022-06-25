import scrapy
#from tutorial import  PostItem
from datetime import datetime,timedelta
from gogonewsanalyze.items import PostItem

class QuotesSpider(scrapy.Spider):
    name = "investirauCameroun"
    root_url="https://www.investiraucameroun.com/"
    is_yesterday_reached=False
    is_first_run=False

    def start_requests(self):

        urls = ["https://www.investiraucameroun.com/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        main parse
        """
        # keywords
        category="immobilier"
        # get  all the single post
        posts = response.css("a")

        for post in posts :
           ## print("short url "+post.attrib['href']) 
            yield scrapy.Request(self.root_url+"/"+post.attrib['href'], callback=self.parse_post)
        #pagination 
        #next_url=""
        ##self.parse(next_url)
        


    def parse_post(self, response):

        
        return PostItem(id = abs(hash(response.url)),
		title = response.css("h2.itemTitle::text").get(),
        url = response.url,
        body = response.css("div.itemIntroText p::text").get(),
        category = str(response.css("span.aidaparentcat_129::text").get()) ,
        creationDate = datetime.now(),
        publishedDate=  datetime.now()
            )

 