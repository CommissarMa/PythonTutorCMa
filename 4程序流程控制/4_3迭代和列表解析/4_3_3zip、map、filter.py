#zip、map和filter函数生成的可迭代对象均有自己的迭代器，
# 可使用next函数执行迭代操作。

#zip函数
# zip函数参数为多个可迭代对象，
# 每次从每个可迭代对象中取一个值组成一个元组，
# 直到可迭代对象中的值取完，
# 生成的zip对象包含了一系列的元组。
x=zip((1,2,3),(10,20,30))#用两个元组参数来解析生成元组系列
next(x)#返回zip对象中的下一个值
next(x)#无对象时，产生StopIteration异常

#map函数
# zip函数参数为多个可迭代对象，
# 每次从每个可迭代对象中取一个值组成一个元组，
# 直到可迭代对象中的值取完，
# 生成的zip对象包含了一系列的元组。
x=map(ord,'abc')#用ord函数返回各个字符串的ASCII码，生成map对象
next(x)#返回map对象中的下一个值

#filter函数
# filter函数与map函数有点类似，
# filter函数用指定函数处理可迭代对象。
# 若函数返回值为真，
# 则对应可迭代对象元素包含在生成的filter对象序列中。
x=filter(bool,(1,-1,0,'ab',(),[],{},(1,2),[1,2],{1,2}))
#筛选出可转换为真的对象
next(x)#返回filter对象中的下一个值
list(x)#将迭代器转换为列表，不包含已迭代的值
