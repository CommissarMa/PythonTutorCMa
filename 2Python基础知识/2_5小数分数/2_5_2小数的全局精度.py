import decimal
from decimal import Decimal
result=Decimal('1')/Decimal('3')#用默认精度计算小数
print(result)
decimal.getcontext().prec=5#设置全局小数精度为5位有效数字
result=Decimal('1')/Decimal('3')
print(result)