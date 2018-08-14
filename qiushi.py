# coding:utf-8
import urllib2
import json
from lxml import etree

url = "https://www.qiushibaike.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

request = urllib2.Request(url, headers=headers)

html = urllib2.urlopen(request).read()

text = etree.HTML(html)

# 返回所有段子的节点位置
node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
items = {}
for node in node_list:
    # 用户名
    # username = node.xpath('./div/a/h2')
    # 图片链接
    image = node.xpath('.//div[@class="author clearfix"]//@src')[0]
    # 内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    # 点赞
    zan = node.xpath('.//i')[0].text
    # 评论
    comments = node.xpath('.//i')[1].text

    items = {
        "image": image,
        "content": content,
        "zan": zan,
        "comments": comments
    }

    with open("qiushi.json", "a") as f:
        f.write(json.dumps(items, ensure_ascii=False).encode("utf-8"))
