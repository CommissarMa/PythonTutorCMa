#将字符串第一个字母大写，其余字幕小写，返回新的字符串
x='this is Python'.capitalize()
print(x)

'abcabcabc'.count('ab')#在整个字符串中ab出现的次数
'abcabcabc'.count('ab',2)#从第3个字符开始ab出现的次数

x='abcdabcd'
x.find('ab')#查找子字符串，返回第一次出现位置的偏移量
x.find('ab',2)#从第3个字符开始查找子字符串
x.find('ba')#没找到就返回-1
#index()方法与find基本一致，只是在未找到子字符串时产生ValueError异常

x.rfind('ab')#返回最后一次出现位置的偏移量

'My name is {0},age is {1}'.format('Tom',23)
#字符串格式化，将字符串中用{}定义的替换域依次用参数args替换

'ab cd ef'.split()#按默认的空格分解
'ab,cd,ef'.split(',')#按指定字符分解