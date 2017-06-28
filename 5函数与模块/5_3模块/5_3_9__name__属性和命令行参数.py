#在作为导入模块使用时，模块__name__属性值为模块文件的主名。
# 当作为顶层模块直接执行时，__name__属性值为“__main__”。

#test7.py
if __name__=='__main__':
    #模块独立运行时，执行下面的代码
    def show():
        print('test7.py独立运行')
    show()
    import sys
    print(sys.argv)#输出命令行参数
else:
    #作为导入模块时，执行下面的代码
    def show():
        print('test7.py作为导入模块使用')
print('test7.py执行完毕！')#该语句总会执行