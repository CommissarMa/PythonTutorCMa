#递归函数时指在函数体内调用函数本身。
def fac(n):#定义函数
    if n==0:
        return 1
    else:
        return n*fac(n-1)#递归调用函数本身
fac(5)