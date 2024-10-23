# encoding=utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup

# https://quotes.toscrape.com/page/2/
base_url = "https://quotes.toscrape.com/"
fp = open("qutoes.txt", "w", encoding="utf-8")
for i in range(1, 6):
    url = base_url + "page/" + str(i) + "/"
    response = requests.get(url)
    response.encoding = "utf-8"
    # html = etree.HTML(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    response.close()
    # text_list = html.xpath('//div[@class="quote"]/span[@class="text"]/text()')
    text_list = soup.select("div.quote span.text")
    for text in text_list:
        text = text.string
        text = text[1: -1]
        fp.write(text + "\n")
fp.close()
print("over~")
