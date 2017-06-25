# Python3中使用Print函数完成基本输出操作
# print函数基本格式如下：
# print([obj1,...][,sep=''][,end='\n'][,file=sys.stdout])

# 1 省略所有参数
print()

# 2 输出一个或多个对象,对象间默认用空格分隔
print(123)
print(123,'abc')

# 3 指定输出分隔符
print(123,'abc','def',sep='%')

# 4 指定输出结尾符合，默认是'\n'
print('abc',end='%')

# 5 输出到文件
# print函数默认输出到标准输出流（即sys.stdout)。
# 可用file参数指定输出到特定文件
file1=open('data.txt','w')#该data.txt文件就在该目录下
print(123,'abc',file=file1)
file1.close()
print(open('data.txt').read())