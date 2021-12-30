# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from nltk.tokenize import casual_tokenize
import json


class HtwEnPipeline:
    def process_item(self, item, spider):
        url = item['url']
        text = item['text']
        # line = '{}\t{}\n'.format(url, casual_tokenize(text))
        # self.file.write(line)
        json_line = json.dumps({"url": url, "text": str.strip(text)}) + "\n"
        self.file.write(json_line)
        return item

    def open_spider(self, spider):
        self.file = open('items.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()
