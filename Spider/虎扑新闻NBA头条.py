# 爬取虎扑新闻 NBA 页面头条数据，
# 并以获取的数据使用 jieba 和 wordcloud 生成云图
import requests
from bs4 import BeautifulSoup
import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud
# 定义 URL,构建请求
url = 'https://nba.hupu.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 '
                  'Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# 头条数据都放在 <div class="list list-news"> 中 , 且均在nba主页中
f_div = soup.find('div',class_='list list-news').find_all('div')
dic = ''
for i in f_div:
    txt = BeautifulSoup.getText(i)
    # 去除无效数据--标点
    remove = ['，', '。', '！', '？', '“', '”', '：', '、', '-', '\n']
    for i in remove:
        txt = txt.replace(i, '')
    # jieba 分词 分割词汇
    txt_cut = jieba.cut(txt)
    dic += " ".join(txt_cut)
print(dic)
# 获取词云生成所需要的模板图片
mask = np.array(Image.open('pink_pig.png'))
# 进行词云的设置
wc = WordCloud(
    width=1000,
    height=700,
    background_color='white',
    font_path='msyh.ttc',   # 词云字体 (微软雅黑)
    mask=mask,  # 所使用的词云图片
    scale=1.5
)
   # stopwords={''} 停用词 --> 可借此去除标点
# 给词云输入文字
wc.generate(dic)
# 词云图保存图片位置
wc.to_file('hupu_NBA_Headlines.png')

print("虎扑新闻NBA页面头条数据-->词云生成成功！")