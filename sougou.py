import requests
import time as t

if __name__=="__main__":
	#指定URL
	t.sleep(2)
	url='https://www.sogou.com'
	#发起请求
	#get方法会返回一个响应对象
	response = requests.get(url=url)
	#获取响应数据
	page_text = response.text
	sougou='sougou.html'
	print(page_text)
	#持久化存储
	with open(sougou,'w+',encoding='utf-8') as fg:
		fg.write(page_text)
	print("爬取数据结束")
