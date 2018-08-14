import scrapy
from ..items import FirstItem


class Lagou(scrapy.Spider):
    name = "sean"
    start_urls = [
        "https://www.lagou.com/"
    ]
    cookie = {
        'user_trace_token': '20180807141940-ddcd5617-9a09-11e8-a341-5254005c3644',
        'LGUID': '20180807141940-ddcd5c34-9a09-11e8-a341-5254005c3644',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'WEBTJ-ID': '20180813084247-16530bc3cd15bc-061b3f0aabdbfc-414a0229-2073600-16530bc3cd279a',
        'JSESSIONID': 'ABAAABAAADEAAFI4821DBE363C395E658B4A8E4213555EF',
        '_gat': '1',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'X_HTTP_TOKEN': '966e6a2bfa9fe37e4fbe358df589db64',
        'TG-TRACK-CODE': 'index_navigation',
        'SEARCH_ID': '3ac844a5291540b8a87649aedb5669db',
        '_gid': 'GA1.2.1317215244.1534120968',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1534128226,1534132117,1534132125,1534139397',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1534143311',
        '_ga': 'GA1.2.1754874847.1533622781',
        'LGSID': '20180813145427-b8aff478-9ec5-11e8-a37b-5254005c3644',
        'LGRID': '20180813145510-d2181f3a-9ec5-11e8-a37b-5254005c3644'
    }

    def parse(self, response):
        for item in response.xpath('//div[@class="menu_box"]/div//a'):
            jobClass = item.xpath('text()').extract()
            jobUrl = item.xpath("@href").extract_first()

            oneItem = FirstItem()
            oneItem["jobClass"] = jobClass
            oneItem["jobUrl"] = jobUrl

            for i in range(30):
                jobUrl2 = jobUrl + str(i + 1)
                try:
                    yield scrapy.Request(url=jobUrl2, cookies=self.cookie, meta={"jobClass": jobClass},
                                         callback=self.parse_url)
                except:
                    pass

    def parse_url(self, response):
        jobClass = response.meta["jobClass"]

        for sel2 in response.xpath('//ul[@class="item_con_list"]/li'):
            jobName = sel2.xpath('div/div/div/a/h3/text()').extract()
            jobPlace = sel2.xpath('div/div/div/a/span/em/text()').extract()
            jobMoney = sel2.xpath('div/div/div/div/span/text()').extract()
            jobNeed = sel2.xpath('div/div/div/div/text()').extract()
            jobNeed = jobNeed[2].strip()
            jobCompany = sel2.xpath('div/div/div/a/text()').extract()
            jobCompany = jobCompany[3].strip()

            jobType = sel2.xpath('div/div/div/text()').extract()
            jobType = jobType[7].strip()

            jobSpesk = sel2.xpath('div[@class="list_item_bot"]/div/text()').extract()
            jobSpesk = jobSpesk[-1].strip()

            Item = FirstItem()

            Item["jobName"] = jobName
            Item["jobPlace"] = jobPlace
            Item["jobMoney"] = jobMoney
            Item["jobNeed"] = jobNeed
            Item["jobCompany"] = jobCompany
            Item["jobType"] = jobType
            Item["jobSpesk"] = jobSpesk
            yield Item
