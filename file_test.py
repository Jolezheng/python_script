import os

file_name='dome.txt'

with open(file_name,'a',encoding='utf-8') as file_obj:
	file_obj.write('hello world,python\n')
	file_obj.write("aaa,bbb,ccc\n")
	file_obj.write("你好，中国\n")
	file_obj.write('*'*9)
	# r=file_obj.write('你好python！\n')
	# print(r)
	# print('%d' %r,file=file_obj)

	
