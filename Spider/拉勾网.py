#拉勾网.py
import urllib.request
import jsonpath
import json
url='https://www.lagou.com/lbs/getAllCitySearchLabels.json'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = request.read()
print(html)

jsonobj = json.loads(html)
city_list = jsonpath.jsonpath(jsonobj,'$..name')
print(city_list)

file = open('city.json','w')
content = json.dump(city_list,ensure_ascii=False)
print(content)
file.write(content)
file.close()







