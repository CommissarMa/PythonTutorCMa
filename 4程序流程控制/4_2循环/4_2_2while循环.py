#while循环在测试条件为真时执行循环体，也称为“当型循环”。
# 如果测试条件一开始就为假，则不会执行循环体。

#while循环基本结构：
#while 测试条件：
#   循环体
#else:
#   语句块
#与for循环类似，可在循环体中使用break和continue语句。
# else部分可以省略。
s=0
n=1
while n<=100:
    s=s+n
    n=n+1
print('1+2+…+100=',s)

#Python允许在while循环的内部使用while循环。