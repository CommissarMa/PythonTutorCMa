len('abcdef')#字符串长度

x='abcdef'
result='ab' in x#字符串包含关系判断
print(result)

#字符串连接
x='12''34''56'#空格分隔的多个字符串可自动合并
print(x)
x='12'+'34'+'56'#用加法运算可将多个字符串合并
print(x)
x='12'*3#乘法运算创建重复的字符串
print(x)

#注意：在使用逗号分隔字符时，会创建字符串组成的元组
x='abc','def'
print(type(x))#元组

#字符串迭代
for a in 'abc':
    print(a)

#索引
x='abcdef'
print(x[0])

#分片
x='abcdef'
print(x[1:4])
print(x[:])
print(x[1:5:2])#最后一个是步长

#使用str函数将数字转换为字符串
str(123)
str(1.23)
str(2+4j)