# coding:utf-8
import threading
# 队列
from Queue import Queue
from lxml import etree
import requests
import json


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # threading.Thread.__init__(self)
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

    def run(self):
        # print "启动" + self.threadName
        while not CRAWL_EXIT:
            try:
                # 取出一个数字
                page = self.pageQueue.get(False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                content = requests.get(url, headers=self.headers)
                self.dataQueue.put(content)
            except:
                pass

        # print "结束" + self.threadName


class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename):
        super(ThreadCrawl, self).__init__()
        # 线程名
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass

    def parse(self,html):
        html = etree.HTML(html)





CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    # 页码的队列，表示10个页面
    pageQueue = Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)
    # 采集结果数据队列（每页的HTML源码）
    dataQueue = Queue()

    filename = open("duanzi.json", "a")

    crawlList = ["采集线程1号", "采集线程2号", "采集线程3号"]
    threadcrawl = []
    # 存储三个线程
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)

    # 解析线程的名字
    parseList = ["解析线程1号", "解析线程2号", "解析线程3号"]
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName, dataQueue, filename)
        thread.start()
        threadparse.append(thread)

    # 等待pageQueue为空
    while not pageQueue.empty():
        pass

    global CRAWL_EXIT
    CRAWL_EXIT = True

    print "pageQueue为空"

    for thread in threadcrawl:
        thread.join()
        print "1"


if __name__ == "__main__":
    main()
