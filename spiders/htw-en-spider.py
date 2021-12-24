from typing import List
import scrapy
from htwen.items import HtwEnItem
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class HtwEnSpider(scrapy.Spider):
    x = 0
    name = "htw-en"
    allowed_domain = ['htw-berlin.de']
    start_urls = ['https://www.htw-berlin.de/en/', 
                 ]
    domain = 'www.htw-berlin.de'
    path_en = '/en/'

    def parse(self, response, **kwargs):
        netloc, path = urlparse(response.url).netloc, urlparse(response.url).path
        if netloc != HtwEnSpider.domain or not path.startswith(HtwEnSpider.path_en):
            return
        self.logger.info('HTW EN spider. RETRIEVING'.format(response.url))

        soup = BeautifulSoup(response.text)
        yield HtwEnItem(url=response.url, text=soup.get_text(separator=" "))

        link_list  = response.xpath('//a')
        for sel in link_list:
            href = sel.attrib['href']
            new_url = urljoin(response.url, href)
            netloc, path = urlparse(new_url).netloc, urlparse(new_url).path
            if netloc == HtwEnSpider.domain and path.startswith(HtwEnSpider.path_en):
                yield response.follow(sel, callback=self.parse)
                pass

