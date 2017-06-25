#使用fractions模块中的Fraction函数来创建
#使用分数可以有效避免浮点数的不精确性
from fractions import Fraction
x=Fraction(2,8)
print(x+2)

#浮点数转分数
x=Fraction.from_float(1.25)
print(x)