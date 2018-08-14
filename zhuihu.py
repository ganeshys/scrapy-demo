# coding:utf-8
from bs4 import BeautifulSoup
import requests


def zhihulogin():
    #  构建一个session对象
    sess = requests.Session()
    headers = {"User-Agent"
               : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

    html = sess.get("https://www.zhihu.com/signup?next=%2F", headers=headers).text
    bs = BeautifulSoup(html, "lxml")
    _xsrf = bs.find("")


if __name__ == "__main__":
    zhihulogin()
