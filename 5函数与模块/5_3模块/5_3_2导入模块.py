#模块需要先导入，然后才能使用其中的变量或函数。
#可使用import或from语句来导入模块，基本格式如下。
#import 模块名称
#import 模块名称 as新名称
#from 模块名称 import导入对象名称
#from 模块名称 import导入对象名称 as新名称
#from 模块名称 import*

#import语句
# import语句用于导入整个模块，
# 可用as为导入的模块指定一个新的名称。
# 使用import语句导入模块后，
# 模块中的对象均以“模块名称.对象名称”的方式来引用。
import math#导入模块
math.fabs(-5)#调用模块函数
math.e#使用模块常量

import math as m#导入模块并制定新名称
m.fabs(-5)#通过新名称调用函数模块
m.e#通过新名称使用模块常量
math.e#模块原名称仍可使用

#from语句
#from语句用于导入模块中的指定对象。
# 导入的对象直接使用，不需要使用模块名称作为限定符。
from math import fabs#从模块导入指定函数
fabs(-5)#直接使用
from math import e#从模块导入指定常量
e
from math import fabs as f1#导入时指定新名称
f1(-10)

#from … import *语句
#使用星号时，可导入模块顶层的全局变量和函数。
from math import *#导入模块顶层全局变量和函数
fabs(-5)#直接使用导入的函数
e#直接使用导入的常量

