# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.exporters import JsonLinesItemExporter


class chongxie(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(chongxie, self).__init__(file, ensure_ascii=None)


