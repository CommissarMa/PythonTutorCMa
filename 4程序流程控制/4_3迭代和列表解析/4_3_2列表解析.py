#列表解析与循环的概念紧密相关
t=[1,2,3,4]
for x in range(len(t)):
    t[x]=t[x]+10
print(t)
#使用列表解析来代替上面的for循环
t=[x+10 for x in t]
print(t)
#列表解析可以用更少的代码来实现相同目的，
#代码运行速度更快

#带条件的列表解析
#可以在列表解析结构末尾使用if头部来执行筛选
[x+10 for x in range(10) if x%2==0]#用if筛选偶数

#多重解析嵌套
[x+y for x in (10,20) if x >10 for y in (1,2,3)]#也可用if筛选

#列表解析用于元组
(x for x in range(10))#生成器
tuple(x*2 for x in range(5) if x%2==1)

#列表解析用于集合
{x for x in range(10) if x%2==1}

#列表解析用于字典
{x:ord(x)for x in 'abcd' if ord(x)%2==0}

#列表解析用于文件
#每次从文件读取一行数据
[x for x in open('d:\\test.txt')]#读得出回车符
[x.strip() for x in open('d:\\test.txt')]#读不出回车符
[x.strip() for x in open('d:\\test.txt') if x[0]=='t']