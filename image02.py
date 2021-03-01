import os
import requests
import re

if __name__ == '__main__':
	#创建一个文件夹，保存所有的图片
	if not os.path.exists('./qiutuLibs'):
		os.mkdir("./qiutuLibs")
	url="https://www.qiushibaike.com/imgrank/"
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
	}
	#使用通用爬虫对url对应的一整张页面进行爬去
	page_text = requests.get(url=url,headers=headers).text

	#使用聚焦爬虫将页面的所有图片进行解析/截取
	ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
	img_src_list = re.findall(ex,page_text,re.S)
	for src in img_src_list:
		#拼接出一个完整的图片url
		src = 'https:'+src
		img_data = requests.get(url=src,headers=headers).content
		#生成图片名称
		img_name = src.split('./')[-1]
		imgPath = './qiutuLibs/'+img_name
		with open(imgPath,'wb') as fp:
			fp.write(img_data)
			print(img_name,'下载成功！！！')
