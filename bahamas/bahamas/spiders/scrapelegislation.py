import scrapy


class ScrapelegislationSpider(scrapy.Spider):
    name = 'scrapelegislation'
    allowed_domains = ['laws.bahamas.gov.bs']
    start_urls = ['http://laws.bahamas.gov.bs/cms/en/legislation/acts.html']

    def parse(self, response):
        """

        There is no pagination but there are buttons, so in this method I add input
        element type 'submit' (which renders as a button) to the URL, I then get all
        submit element values (A-Z) and iteratively add each value as a param. The 
        new URL is sent to parse_acts method.
        
        """

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

            # 3. Extract the URL (href attribute) of the document link in the row
            href = row.css('td.hasTip a::attr(href)').get()

            # 4. Ensure that the source_url is complete, i.e starts with "http://laws.bahamas.gov.bs"
            source_url = ("http://laws.bahamas.gov.bs" + href)

            yield {
                "title": title,
                "source_url": source_url
            }



        
