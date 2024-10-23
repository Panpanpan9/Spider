import scrapy
from quotes.items import QuotesItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        saying_list = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').getall()
        author_list = response.xpath('//div[@class="quote"]/span/small[@class="author"]/text()').getall()
        for i in range(len(saying_list)):
            saying = saying_list[i]
            author = author_list[i]
            item = QuotesItem()
            item["saying"] = saying
            item["author"] = author
            yield item
