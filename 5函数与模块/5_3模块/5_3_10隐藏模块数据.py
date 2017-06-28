#在使用from…import *导入模块变量时，
#默认会将模块顶层的所有变量名导入。
#例外情况是，以单个下划线开头的变量（如_abc）不会被导入。

#test8.py
x=100
_y=[1,2]
def _add(a,b):
    return a+b
def show():
    print('out from test8.py')