import requests
import json

if __name__=="__main__":
	#指定url
	url='https://fanyi.baidu.com/langdetect'
	#UA伪装，将对应的User-Agent封装到一个字典中
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
	}
	#处理url携带的参数，封装到字典中
	kw=input('请输入翻译的词：')
	param={
		'query': kw
	}
	#对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
	response=requests.get(url=url,params=param,headers=headers)
	list_data = response.json()
	#获取响应数据
	page_text=response.text
	fileName = kw + '.json'
	#持久化存储
	# with open(fileName,'w',encoding='utf-8') as fg:
	# 	fg.write(page_text)
	fy=open(fileName,'w',encoding='utf-8')
	json.dump(list_data, fp=fy,ensure_ascii=False)
	print('保存成功！！！')