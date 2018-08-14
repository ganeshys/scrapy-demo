import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readline()
print(data)
print(dataline)
