import requests
import json

if __name__=="__main__":
	#1.UA伪装：将对应的User-Agent封装到一个字典中
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
	}
	#2.指定URL
	post_url='https://m.douban.com'
	param={
		"pe": "movie",
		"tag": "热门",
		"sort": "recommend",
		"page_limit": "20",
		"page_start": "0",
	}
	
	#3.请求发送
	response = requests.get(url=post_url,params=param,headers=headers)
	list_data = response.json()
	
	fileName='./douban.json'
	#4.持久化存储
	fp=open(fileName,'w',encoding='uts-8')
	json.dump(list_data,fp=fp,ensure_ascii=False)
		
	print("保存成功")


		

		