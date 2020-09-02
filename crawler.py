import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import tldextract
import csv

class Spider(CrawlSpider):
    
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'DEPTH_LIMIT': 1
    }

    counter = 0

    searchPhrases = [
        "HubSpot",
        "HubspotFormWrapper",
        "!-- start coded_template",
        "!-- Start of HubSpot Analytics Code",
    ]

    name = 'go.everquote.com'
    allowed_domains = None
    start_urls = None
    
    rules = (
        # Extract and follow all links!
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    csv_columns = ["URL", "domain", "subdomain"] + searchPhrases
        
    # with open('outfile.csv', "w") as out_file:   
    #     writer = csv.writer(out_file)
    #     writer.writerow(csv_columns)   

    report = []

    result = []

    def parse_item(self, response):

        URL = format(response.url) 
        print(URL)
        print("XXXXXXXXXXX")
        # print(self.allowed_domains)
        print("XXXXXXXXXXX")
        # print(self.start_urls)
        print("XXXXXXXXXXX")

        row = {}
        extracted = tldextract.extract(URL)
        row["URL"] = URL
        row["domain"] = extracted.domain
        row["subdomain"] = extracted.subdomain

        self.counter = self.counter + 1
        # row["No."] = self.counter

        
        # with open('outfile.csv', "a") as out_file:   
            # writer = csv.writer(out_file)
        for searchPhrase in self.searchPhrases: 
            if searchPhrase in response.body.decode("utf-8"):
                row[searchPhrase] = 1
            else:
                row[searchPhrase] = 0

        self.result.append(
            tuple(row.values())
        )       
            
    def getResults(self):
        return(self.result)

            # # for key, value in row.items():
            # writer.writerow(row.values())    