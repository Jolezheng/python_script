import requests

if __name__ == '__main__':
	#指定url
	url='http://www.nipic.com/'
	#发起请求
	image_data = requests.get(url=url).content

	#获取响应数据
	with open('./tupian.jpg','wb') as fg:
		fg.write(image_data)
	print("get numbus over!!!")