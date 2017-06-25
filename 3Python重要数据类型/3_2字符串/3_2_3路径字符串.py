'd:\temp\a.py'#错误，\t会被转义
r'd:\temp\a.py'#使用raw字符串，Python不会解析其中的转义字符
'd:\\temp\\a.py'#正确路径
'd:/temp/a.py'#正确路径