#在迭代字符串、列表等序列时已经用到了for循环。
# for循环是Python中的一个通用的序列迭代器，
# 可以遍历序列对象中的所有对象。

#for循环基本格式：
#for var in object：
#   循环体语句块
#else:
#   语句块
#else部分可以省略。
#for执行时，依次将可迭代对象object中的值赋值给变量var。
# var每赋值一次，则执行一次循环体语句块。
# 循环执行结束时，如果有else部分，则执行对应的语句块。
# else部分只在正常结束循环时执行。
# 如果用break跳出循环，则不会执行else部分。
for x in (1,2,3,(4,5)):
    print(x)#用x迭代元组中的对象，其中包含了一个嵌套的子元组
else:
    print("finish")

#可以使用range函数来生成包含连续多个整数的range对象
range(3)#0到2
range(-2,2)#-2到2
range(-2,2,2)#step为2

#多个变量迭代
for (a,b) in ((1,2),(3,4),(5,6)):
    print(a,b)

#break与continue
#与Java，C语言一样
#唯一区别在于使用break后不会执行else的语句块

#嵌套使用for循环
print(1,2,3,end="")
for x in range(4,100):
    for n in range(2,x):
        if x%n==0:
            break
    else:
        print(x,end="")
else:
    print("over")