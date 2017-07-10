class testclass:
    data=100
    def setpdata(self,value):
        self.pdata=value
    def showpdata(self):
        print('self.pdata=',self.pdata)
    print('类testclass加载完成！')

#在Python中，实例对象继承了类对象的所有属性和方法，
#可以用dir()函数来查看对象的属性和方法。

#1.共享属性
#类对象的数据属性是全局的，即默认情况下它属于类对象，
#并可通过实例变量来引用。
x=testclass()
print(x.data)

#2.实例对象的“私有”属性
#实例对象的“私有”属性指类的函数中以“self.属性名=值”格式进行赋值创建的属性。
#“私有”强调属性只属于当前实例对象，对其他实例对象而言是不可见的。
#实例对象一开始是“空”的，只有在调用了类对象的方法后，
# 才会通过其中的赋值语句创建“私有”属性。
x=testclass()
#x.pdata#试图访问实例对象的属性，结果显示属性不存在
x.setpdata(123)
x.pdata#赋值后，就可以访问属性了

#3.对象的属性是动态的
#Python总是在第一次给变量赋值时创建变量。
#对于类对象或实例对象而言，当给不存在的属性赋值时，
#Python为其创建属性。
testclass.data2='abc'#赋值，为类对象添加属性
x.data3=[1,2]#赋值，为实例对象添加属性
print(testclass.data2,x.data2,x.data3)#显示属性值
print(dir(testclass))#查看类对象属性列表
print(dir(x))#查看实例对象属性列表

