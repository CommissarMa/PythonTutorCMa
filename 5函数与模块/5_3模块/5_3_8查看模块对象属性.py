#在导入模块时，Python会使用模块文件创建一个模块对象。
#模块中引用各种对象的变量名称为对象的属性。
#Python也为模块对象添加一些内置的属性。
#可使用dir函数来查看对象属性。

#导入模块test6，查看其属性：
import test6
print(dir(test6))
print(test6.__doc__)#返回文件开头的文档注释
print(test6.__file__)#返回模块完整文件名
print(test6.__name__)#显示模块名称

