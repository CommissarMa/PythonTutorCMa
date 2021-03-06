#Python中的各种序列（字符串、列表、元组、字典以及文件等）
# 均可作为可迭代对象，可迭代对象可以使用迭代器来遍历包含的元素。
#字符串、列表、元组以及字典等对象虽然是可迭代对象，
# 但它们没有自己的迭代器。
#Python使用iter()函数来生成可迭代对象的迭代器，
# 然后对迭代器调用next()函数来遍历对象。
# next()函数依次返回可迭代对象的一个元素，
# 无元素返回时，会产生一个StopIteration异常。
d=iter([1,2,3])#为列表生成迭代器
next(d)#返回第一个元素
next(d)#返回第二个元素
next(d)#返回第三个元素
next(d)#当无元素返回时，产生异常

d=iter((1,2,(3,4)))#使用迭代器迭代元组
next(d)
next(d)
next(d)
#还可以迭代字符串，字典（只能迭代键，要迭代键值对或值时请参考字典中的方法）
#文件对象有自己的迭代器:_next()_方法
mf=open('d:\\test.txt')
mf.__next__()#读下一行
mf.__next__()#读下一行
mf.__next__()#读下一行
mf.__next__()#读下一行，已无数据，出错
#也可用next()函数来调用文件对象的迭代器
mf=open('d:\\test.txt')
next(mf)

