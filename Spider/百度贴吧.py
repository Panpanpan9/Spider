# encoding=utf-8
import urllib.request

_name_='传播智客'
if _name_== "_main_":
    kw = input("请输入需要爬取的贴吧名：")
    begin_page = int(input("请输入起始页："))
    end_page = int(input("请输入结束页"))
    url = 'https://tieba.baidu.com/f?'
    key = urllib.parse.urlencode({"kw":kw})
    url = url + key
    tieba_spider(url,begin_page,end_page)

    def tieba_spider(url, begin_page, end_page):
        for page in range(begin_page, end_page + 1):
            pn = (page-1)*50
            file_name = "第"+str(page)+"页.html"
            html = local_page(full_url, file_name)
            write_page(html, file_name)

    def local_page(url,file_name):
        headers = {
            "User-Agent": "FireFox"
        }
        request = urllib.request(url,headers=headers)
        return urllib,request.urlopen(request).read()

    def write_page(html,file_name):
        print("正在保存"+file_name)
        with open(file_name,'w',encoding='utf-8') as file:
            file.write(html.decode('utf-8'))

    request = urllib.request.Request(url, headers=headers)
    # # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)
    # 获取响应中的页面中的源码   read()返回的是字节形式的二进制数据
    content = response.read().decode("utf-8")
    # 关闭响应
    response.close()
    # 打印数据
    print(content)

