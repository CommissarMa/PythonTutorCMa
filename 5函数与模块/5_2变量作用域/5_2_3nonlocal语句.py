#nonlocal语句与global语句类似，
#它声明变量是外部的本地变量。
def test():
    a=10#创建test函数的本地变量a
    def show():
        nonlocal a#声明a是test函数的本地变量a
        a=100#修改test函数的本地变量a
        print('show()函数内使用test函数的本地变量a,a=',a)
    show()
    print("test()函数内使用test函数的本地变量a,a=",a)
test()
