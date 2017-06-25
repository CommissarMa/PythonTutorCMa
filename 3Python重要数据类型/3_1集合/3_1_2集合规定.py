#集合中的元素不允许有重复值，
#在创建集合对象时，Python会自动去除重复值
x={1,1,2,2}
print(x)#{1,2}

#集合解析构造方法
y={x for x in [1,2,3,4]}
print(y)
y={x for x in 'abcd'}
print(y)#打印出来的字母顺序是随机的

#还可以用解析对象的表达式来创建集合元素
y={x**2 for x in [1,2,3,4]}
print(y)
y={x*2 for x in 'abcd'}
print(y)#顺序随机
