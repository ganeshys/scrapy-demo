# coding:utf-8
import scrapy

from ..items import TencentItem


class TecentpositionSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    url = "https://hr.tencent.com/position.php?lid=&tid=&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentItem()
            # 职位名
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
        if self.offset < 3500:
            self.offset += 10
        # 自增10
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
