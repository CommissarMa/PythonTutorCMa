import decimal
from decimal import Decimal
result=Decimal('1')/Decimal('3')#用默认精度计算小数
print(result)
with decimal.localcontext() as local:#with语句创建临时的上下文
    local.prec=3#设置临时小数精度为3位有效数字
    result=Decimal(1)/Decimal(3)
    print(result)
result=Decimal(1)/Decimal(3)#with临时上下文外都是默认精度
print(result)