#如果直接用文本文件或二进制文件格式直接存储Python中的各种对象，
#通常需要进行繁琐的转换。
#可以使用Python标准模块pickle处理文件中对象的读写。
x=[1,2,'abc']#创建列表对象
y={'name':'John','age':25}#创建字典对象
myfile=open('d:\\objdata.bin','wb')#以wb方式打开文件
import pickle#导入pickle模块
pickle.dump(x,myfile)#将列表对象写入文件
pickle.dump(y,myfile)#将字典对象写入文件
myfile.close()#关闭文件
myfile=open('d:\\objdata.bin','rb')#重新以rb方式打开文件
myfile.read()#读出文件中的全部内容
myfile.seek(0)#文件指针移动到文件开头
x=pickle.load(myfile)#从文件中加载对象（列表）
x=pickle.load(myfile)#从文件中加载对象（字典）