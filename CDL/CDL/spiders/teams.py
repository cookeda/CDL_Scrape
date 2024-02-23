import scrapy

BASE = "cdl.game5.gg"

class TeamsSpider(scrapy.Spider):
    name = "teams"
    allowed_domains = ["cdl.game5.gg"]

    def start_requests(self):
        start_urls = [
            "http://cdl.game5.gg/teams",
        ]

        for url in start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
#        for x in range(1, len(response.css('li.product__item'))+1):
        
        name = response.css('li.product__item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)::text').get()
            #link = response.css(f'div:nth-child({x}) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)::attr(href)').get()
        yield {
                'Name': name,
            #    'Link': link    
            }