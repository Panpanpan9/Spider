import urllib.request
request = urllib.request.Request("https://www.baidu.com", headers={"User-Agent": 'Chrome'})
response = urllib.request.urlopen(request)
content = response.read()
response.close()
print(content)
with open("baidu.html", "wb")as f:
    f.write(content)
print("百度首页爬取成功")