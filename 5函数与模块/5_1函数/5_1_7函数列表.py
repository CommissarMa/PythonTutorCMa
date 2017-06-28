#Python允许使用将函数作为列表对象，然后通过列表索引来调用函数。
d=[lambda a,b:a+b,lambda a,b:a*b]#使用lambda函数建立列表
d[0](1,3)#调用第一个函数
d[1](1,3)#调用第二个函数
#当然除了lambda函数，也可以使用def定义函数，然后用函数名构成列表。

#Python还允许使用字典来建立函数映射
def add(a,b):
    return a+b
def fac(a):
    if a==0:
        return 1
    else:
        return a*fac(a-1)
d={'求和':add,'求阶乘':fac}
d['求和'](1,2)#调用求和函数
d['求阶乘'](5)#调用求阶乘函数