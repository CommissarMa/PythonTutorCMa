#简单if语句
x=5
if x>0:
    print(x,'是正数')

#双分支if语句
x=-5
if x>0:
    print(x,'是正数')
else:
    print(x,'不是正数')

#多分支if语句
x=85
if x<60:
    print('不及格')
elif x<70:
    print('及格')
elif x<90:
    print('中等')
else:
    print('优秀')