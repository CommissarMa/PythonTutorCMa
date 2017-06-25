x={1,2,'a','bc'}
y={1,'a',5}
print(len(x))#求集合中元素个数
print('a' in x)#判断是否属于集合
print(x-y)#求差集
print(x|y)#求并集
print(x&y)#交集
print(x^y)#对称差，即x-y与y-x的并集
print(x<y)#判断x是否为y的子集
print({1,2}<x)