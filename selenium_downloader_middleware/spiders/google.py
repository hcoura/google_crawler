# -*- coding: utf-8 -*-
import scrapy
from ..items import Item


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com.br']
    start_urls = [
        'https://www.google.com.br/?#safe=off&q=selenium',
        'https://www.google.com.br/#q=selenium&safe=off&start=10',
        'https://www.google.com.br/#q=selenium&safe=off&start=20',
        'https://www.google.com.br/#q=selenium&safe=off&start=30',
    ]

    def parse(self, response):
        links = response.xpath("//h3[@class='r']/a/@href").extract()
        for l in links:
            yield Item({"link": l})
