from crawler import Spider
from db_handler import DbHandler
import scrapy
from scrapy.crawler import CrawlerProcess

# input_handler = XlsHandler('./hubspot_list.xlsx','Meta Data')


db = DbHandler()

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

temp_url_list = db.getUrls()
domain_list = db.getDomains()
url_list = []


for item in temp_url_list:
    if item != None:
        for url in item.split(";"):
            url_list.append("https://" + url)

print(domain_list)
print(url_list)
class MySpider(Spider):
    allowed_domains = domain_list
    start_urls = url_list


process.crawl(MySpider)
process.start()

db.putToDb("crawlerResult", MySpider.getResults(MySpider))

# print(MySpider.put_to_db())