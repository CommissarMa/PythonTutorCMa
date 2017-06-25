#共享引用指多个变量引用了同一个对象

#示例1
x=5
y=x#x,y都引用了对象5

#示例2
x=[1,2,3]
y=x
x[0]=['abc']
print('x=',x)
print('y=',y)
print(x is y)#is用于判断两个变量是否引用了同一个对象

#示例3
x=5
a=5
print(x is a)