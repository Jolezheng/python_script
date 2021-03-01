from lxml import etree
import requests
import os

if __name__ == '__main__':
	url = 'http://pic.netbian.com/4kmeinv/'
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
	}
	#手动设定响应数据的编码格式
	#response.encoding = 'utf-8'
	response = requests.get(url=url,headers=headers)
	page_text =response.text
	#数据解析：src的属性值，alt属性
	tree = etree.HTML(page_text)
	li_list = tree.xpath("//div[@class='slist']/ul/li")

	#创建一个文件夹
	if not os.path.exists('./piclibs'):
		os.mkdir('./piclibs')

	for li in li_list:
		img_src = 'http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
		img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
		#通用处理中文乱码解决方案
		img_name = img_name.encode('iso-8859-1').decode('gbk')
		#请求图片进行持久化存储
		img_data = requests.get(url=img_src,headers=headers).content
		img_path = 'piclibs/'+img_name
		with open(img_path,'wb') as fp:
			fp.write(img_data)
			print(img_name,'下载成功！！！')
