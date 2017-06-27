#copy方法
x={'name':'John','age':25}
y=x#直接赋值时，x和y引用同一个字典
print(x,y)
y['name']='CommissarMa'
print(x,y)
print(y is x)#判断是否引用同一对象
y=x.copy()#y引用复制的字典
y['name']='Mary'#修改y引用的字典映射值，此时不影响x的引用
print(x,y)
print(y is x)#判断是否引用同一对象

#删除全部字典对象
x=dict(name='John',age=25)
x.clear()#结果为空字典{}

#获取映射值
x={'name':'John','age':25}
print(x.get('name'))#返回映射值
x.get('sex')#不存在的键返回空值
x.get('sex','male')#不存在的键返回指定值

#从字典中删除键，并返回映射值。若键不存在，则返回default
x={'name':'John','age':25}
x.pop('name')#删除键并返回映射值
x.pop('sex','male')#删除不存在的键，则返回指定的值
x.pop('sex')#如果没指定值，则出错KeyError

#从字典删除并返回键值对元组。
#空字典调用该方法会产生KeyError错误。
x={'name':'John','age':25}
x.popitem()#删除并返回键值对元组

#setdefault
x={'name':'John','age':25}
x.setdefault('name')#返回指定键的映射值
x.setdefault('sex')#键不存在，为字典添加键值对，映射值默认为None
x.setdefault('phone','123456')#添加键值对

#update
#该方法用于为字典添加键值对。参数other可以是另一个字典或用
#赋值格式表示的元组。若字典已存在同名的键，则映射值被覆盖。
x={'name':'John','age':25}
x.update({'age':30,'sex':'male'})#添加键值对，并覆盖同名键的映射值
x.update(name='Mike')#修改映射值
x.update(code=110,address='NewStreet')#添加键值对