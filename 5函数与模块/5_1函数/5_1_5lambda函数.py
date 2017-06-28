#lambda函数也称表达式函数，用于定义一个匿名函数，
#可将该函数赋值给变量，通过变量调用。
#lambda函数定义的基本格式如下。
#lambda 参数表：表达式
add=lambda a,b:a+b#定义表达式函数，赋值给变量
add(1,2)#函数调用格式不变

#lambda函数也充分说明了Python中的函数名就是一个变量，
#该变量引用了一个函数对象。
#lambda函数非常适合定义简单的函数，与def不同，
#lambda的函数体只能是一个表达式，可以调用其他的函数，
#但不能使用Python的其他语句
add=lambda a,b:ord(a)+ord(b)#在lambda表达式中调用其他的函数
add('1','2')
