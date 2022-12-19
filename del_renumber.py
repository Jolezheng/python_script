import pandas as pd
import xlrd


#df = pd.read_excel(path01)
fa = open("C:\\Users\\guosen\\Desktop\\111\\repo_product.txt")
a = fa.readlines()
print(a)
fa.close()



fb = open("C:\\Users\\guosen\\Desktop\\111\\254.txt")
b = fb.readlines()
print(b)
fb.close()

"""
for i in a:
    if i in b:
        print(i)
        c = i
        fc = open("C:\\Users\\guosen\\Desktop\\111\\result.txt", "w")
        fc.writelines(c.strip())
        print(c)
        fc.close()


"""
c = [i for i in a if i not in b]

fc = open("C:\\Users\\guosen\\Desktop\\111\\result.txt", 'w')
fc.writelines(c)
print(c)
fc.close()


"""
line = f.readline() #每次读取一行内容
line = old.readline() #每次读取一行内容
print(line, '\n')
for line in old:
    print(line.strip())

f.close()
"""

exit(1)



