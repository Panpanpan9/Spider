# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesPipeline:

    def process_item(self, item, spider):
        saying = item["saying"]
        author = item["author"]
        with open("quotes.txt", "a", encoding="utf-8") as fp:
            fp.write("author:" + author + ", saying:" + saying + "\n")
        return item

class QuotesDownloadPipeline:
    pass
