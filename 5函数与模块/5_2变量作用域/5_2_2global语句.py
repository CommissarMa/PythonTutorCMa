#global语句用于在函数内部声明全局变量
def show():
    global a
    a=10
    print('a=',a)#声明a是函数外部的一个全局变量
    a=100
    print('a=',a)
show()
print(a)