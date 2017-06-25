#小数对象使用decimal模块中的Decimal函数来创建
#使用时应先导入函数
from decimal import Decimal
result=Decimal('0.3')+Decimal('0.3')+Decimal('0.3')+Decimal('0.1')
print(result)#小数对象是带精度的，因此输出结果为1
result=0.3+0.3+0.3+0.1
print(result)#由于浮点数的误差，输出结果并不为1