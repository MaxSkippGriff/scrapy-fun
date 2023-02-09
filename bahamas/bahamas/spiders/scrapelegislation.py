import scrapy


class ScrapelegislationSpider(scrapy.Spider):
    name = 'scrapelegislation'
    allowed_domains = ['laws.bahamas.gov.bs']
    start_urls = ['http://laws.bahamas.gov.bs/cms/en/legislation/acts.html']

    def parse(self, response):
        pass
