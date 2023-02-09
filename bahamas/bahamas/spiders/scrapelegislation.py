import scrapy


class ScrapelegislationSpider(scrapy.Spider):
    name = 'scrapelegislation'
    allowed_domains = ['laws.bahamas.gov.bs']
    start_urls = ['http://laws.bahamas.gov.bs/cms/en/legislation/acts.html']

    def parse(self, response):

        # URL with input element type submit without element value
        page = "https://laws.bahamas.gov.bs/cms/en/legislation/acts.html?view=acts_only&submit4="

        # Get all alphabetical button values - letters A-Z
        alphabet_buttons = response.css('input[name="submit4"]::attr(value)').getall() 

        # Loop through each element value (A-Z)
        for button in alphabet_buttons:
            # Add value as param to URL
            parse_page = page + button
            # Pass url to parse_acts to extact data
            yield response.follow(parse_page, callback=self.parse_acts)

    
    def parse_acts(self, response):

        # 1. Write a CSS selector that finds all of the table rows
        for row in response.css('tr.row0'):

            # 2. Extract the title of the document link from the row
            title = row.css('td.hasTip a::text').get().strip()

            yield {
                "title": title
            }


        
