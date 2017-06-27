#Python与C/C++在处理真值和逻辑运算的方式上有所不同。
#在Python中：
#任何非0数字和非空对象都为真。
#数字0、空对象（如空列表[]、空字典{}）None都为假
#比较和相等测试返回True（真）或False（假）
#逻辑运算and和or会返回参与运算的真或假的对象。

#比较和相等测试总是返回True或False。
print(2<5)
print(2>5)
print(2==5)

#not运算返回True或False。
not True,not False
not 0,not 1,not 2#非0数字为真
not 'abc',not [1,2],not{'a':12}#非空对象为真
not "",not [],not{}#空的对象为假

#and和or运算符总是返回参与运算的对象，
#而不是True或False
#Python在计算and运算时，总是按从左到右的顺序计算。
#在找到第一个为假的对象时，返回该对象，即使右侧还有需要计算的对象，计算都结束。
#这种计算方式称为短路计算。如果参与运算的对象都为真，则返回最后一个为真的对象。
