import requests#引入request库
from lxml import etree#引入xpath定位需要的库

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}#浏览器请求头

def get_baidu_more():

    for i in range(1):#套用的自己以前的模板

        url = 'https://www.baidu.com/more/'

        rs = requests.session()#定义对象
        r = rs.get(url, headers=headers)#get方法传参

        r.encoding = 'utf-8'#使用utf-8解码，不然会出现乱码
        trees = etree.HTML(r.text)#解析文本

        data=[]#储存功能的几种酚类
        for i in range(1, 9):#看了看一共九种
            Theclass = trees.xpath('//*[@id="content"]/h3[{}]/text()'.format(i))#定位
            data.append(Theclass[0])#添加到新的列表中
        #print(data)#输出测试

        j=0
        for i in range(1,90):#爬取每一个功能对应的标签
            name = trees.xpath('//*[@id="content"]/div[{}]/div[2]/a/text()'.format(i))#功能名称
            link = trees.xpath('//*[@id="content"]/div[{}]/div[2]/a/@href'.format(i))#功能对应的链接
            what = trees.xpath('//*[@id="content"]/div[{}]/div[2]/span/text()'.format(i))#功能描述
            if(name==[]):#当标签内容为空则为大类标签的位置，补全分类
                print(data[j])
                j=j+1
                print(" ")
            else:
                print(name[0])
                print(link[0])
                print(what[0])
                print(" ")

get_baidu_more()


