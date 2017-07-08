#类定义的基本格式：
"""
class 类名:
    赋值语句
    赋值语句
    ……
    def语句定义函数
    def语句定义函数
    ……
"""
#实例
class testclass:
    data=100
    def setpdata(self,value):
        self.pdata=value
    def showpdata(self):
        print('self.pdata=',self.pdata)
    print('类testclass加载完成！')