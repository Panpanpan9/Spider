# 爬取百度首页爬虫
import urllib.request
# 定义 URL,构建请求
url = 'https://www.baidu.com'
# 浏览器请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 '
                  'Safari/537.36'
}
request = urllib.request.Request(url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应中的页面中的源码   read()返回的是字节形式的二进制数据
content = response.read().decode('utf-8')
# 关闭响应
response.close()
# 将爬取到的信息存储在本地磁盘上
with open('baidu.html', 'w', encoding='utf-8')as f:
     f.write(content)
# 打印数据
print('百度首页爬取成功！')
print(content)