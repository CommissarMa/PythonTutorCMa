# Python使用缩进（空格）来表示代码块
# 通常、语句末尾的冒号表示代码块的开始
x=1
if x>0:
    print("yes")
else:
    print("no")

# 在包含代码嵌套时，应注意同级代码块的缩进量应保持相同
x=-1
if x>0:
    print("x>0")
    if x>2:
        print("x>2")
else:
    print("x<=0")