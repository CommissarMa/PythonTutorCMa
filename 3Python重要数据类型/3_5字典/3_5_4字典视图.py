#字典的items()、keys()和values()方法用于返回字典键值对的视图对象。
#视图对象支持迭代操作，并可反映未来对字典的修改。
#视图对象不是列表，不支持索引。
#通常用list()方法将视图对象转换为列表。

#items()方法返回键值对视图
x={'name':'John','age':25}
y=x.items()#返回键值对视图dict_items
for a in y:
    print(a)#迭代键值对视图
x['age']=30#修改字典
print(y)#从显示结果可以看出视图反映了字典中的修改内容
print(list(y))#将键值对视图转换为列表

#keys()方法返回字典中所有键的视图。
x={'name':'John','age':25}
y=x.keys()#返回键的视图
x['sex']='male'#添加键值对
print(y)#显示结果说明键视图包含了新添加的键
print(list(y))#将键视图转换为列表

#values()方法返回字典中全部值的视图。
x={'name':'John','age':25}
y=x.values()#返回字典的值视图
x['sex']='male'#添加键值对
print(y)#值视图包含了新添加的值
print(list(y))#将值视图转换为列表

#键视图支持各种集合运算，键值对视图和值视图不支持集合运算。
x={'a':1,'b':2}
kx=x.keys()#返回x的键视图
y={'b':3,'c':4}
ky=y.keys()#返回y的键视图
kx-ky#求差集
kx|ky#并集
kx&ky#交集
kx^ky#对称差集