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
        for team in response.css('li.product__item'):
            name = team.css('h2 > a::text').get()  # Extract the team name
            yield {'name': name} 
