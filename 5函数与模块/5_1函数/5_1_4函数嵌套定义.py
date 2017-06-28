#Python允许在函数内部定义函数。
def add(a,b):
    def getsum(x):#在函数内部定义的函数，将字符串转换为ASCII求和
        s=0
        for n in x:
            s+=ord(n)
        return s
    return getsum(a)+getsum(b)#调用内部定义的函数getsum
add('12','34')#调用函数
#注意：内部定义的函数，也只能在函数内部使用。