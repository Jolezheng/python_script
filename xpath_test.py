from lxml import etree
# import requests

if __name__ == '__main__':
	tree = etree.parse('chi.html')
	# r = tree.xpath('/html/body/div')
	# r = tree.xpath('/html//div')
	r = tree.xpath('//div')
	# r = tree.xpath('/html//div[@class="pc module"]')
	# r = tree.xpath('//div[@class="XXX"]//li[5]/a/text()')[0]
	# r = tree.xpath('//div[@class="XXX"]//li[5]/a/text()')[0]
	# r = tree.xpath('li[7]//text()')
	# r = tree.xpath('//div[@class="XXX"]/img/@src')
	# r = tree.xpath('/html/body/title/text()')[0]
	print(r)


