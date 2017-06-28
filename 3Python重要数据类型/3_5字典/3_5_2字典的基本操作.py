#创建字典
dict()#创建空字典
{'name':'John','age':25,'sex':'male'}#使用字典常量
{'book':{'Python编程':100,'C++入门':99}}#使用嵌套的字典
{1:'one',2:'two'}#用数字作为键
{(1,3,5):10,(2,4,6):50}#用元组作为键
dict(name='John',age=25)#使用赋值格式的键值
dict([('name','age'),('John',25)])#使用包含键元组和值元组的列表创建字典
dict.fromkeys(['name','age'])#创建无映射值的字典，默认值为None
dict.fromkeys(['name','age'],0)#创建值相同的字典
dict.fromkeys('abc')#使用字符串创建无映射值的字典
dict(zip(['name','age'],['John',25]))#使用zip解析键值列表创建字典

x={}
x['name']='John'#通过赋值
x['age']=25

len(x)#返回字典中键值对的个数

'name' in x#in操作符用于判断字典是否包含某个键

x['name']='CommissarMa'#支持索引和修改映射值