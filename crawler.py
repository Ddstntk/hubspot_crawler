import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import tldextract
import csv


# class TestSpider(scrapy.Spider):
#     name = "test"

#     start_urls = [
#         "http://stackoverflow.com/questions/38233614/download-a-full-page-with-scrapy",
#     ]


#     def parse(self, response):
#         filename = response.url.split("/")[-1] + '.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)


class MySpider(CrawlSpider):
    
    custom_settings = {
        'LOG_LEVEL': 'INFO',
    }

    counter = 0

    searchPhrases = [
        "HubSpot",
        "HubspotFormWrapper",
        "!-- start coded_template",
        "!-- Start of HubSpot Analytics Code",
    ]



    name = 'go.everquote.com'
    allowed_domains = ['everquote.com']
    start_urls = ['https://go.everquote.com/']

    rules = (
        # Extract and follow all links!
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    csv_columns = ["URL", "domain", "subdomain"] + searchPhrases
        
    with open('outfile.csv', "w") as out_file:   
        writer = csv.writer(out_file)
        writer.writerow(csv_columns)   

    report = []

    def parse_item(self, response):
        URL = format(response.url) 
        row = {}
        extracted = tldextract.extract(URL)
        row["URL"] = URL
        row["domain"] = extracted.domain
        row["subdomain"] = extracted.subdomain

        self.counter = self.counter + 1
           
        with open('outfile.csv', "r+") as out_file:   
            writer = csv.writer(out_file)
            for searchPhrase in self.searchPhrases: 
                if searchPhrase in response.body.decode("utf-8"):
                    row[searchPhrase] = "Y"
                else:
                    row[searchPhrase] = "N"
            
            

            # for key, value in row.items():
            writer.writerow(row.values())    