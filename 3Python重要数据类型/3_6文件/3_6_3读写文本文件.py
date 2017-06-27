#首先在d盘下新建一个test.txt文件
#内容如下：
#one 第一行
#two 第二行
#three 第三行

#以r方式打开文件读数据
myfile=open('d:\\test.txt')#以默认读方式打开文件
x=myfile.read()#读文件全部内容到字符串
print(x)
print(myfile.read())#文件指针已指向文件末尾，返回空字符串
myfile.seek(0)#将文件指针移动到文件开头
x=myfile.read(5)#读5个字节到字符串
print(x)
myfile.tell()#返回文件指针当前位置
myfile.readline()#读第一行剩余部分
myfile.readline()#读下一行
myfile.seek(0)
myfile.readlines()#读文件全部内容到列表
myfile.seek(0)
for x in myfile:
    print(x)#以迭代方式读文件
#输出结果看一下，思考为什么两行文字之间有一个空行
myfile.close()#关闭文件

#r+方式打开文件
#以r+方式打开文件时，可从文件读取数据或向文件写入数据。
#在写入数据前，应先使用seek()方法设置数据写入位置。
#如果在read()等方法读出数据后执行写入操作，数据会写入到文件末尾。
myfile=open('d:\\test.txt','r+')#以r+方式打开文件，文件指针指向文件开头
myfile.write('oneline\n')#从文件开头写入7个字符
myfile.seek(0)#定位到文件开头
print(myfile.read())#读出全部数据
myfile.seek(7)#将文件指针指向第8个字节（位置为7）
myfile.write('123')#写入数据
myfile.seek(0)
myfile.read()#读出数据，查看前面写入的数据
myfile.seek(0)
myfile.read(5)#读出5个字符
myfile.write('xxx')#写入数据，读出数据后立即写入，数据写入文件末尾
myfile.seek(0)
print(myfile.read())#读出数据，查看"xxx"在文件末尾
myfile.close()#关闭文件

#以w方式打开文件
#以w方式打开文件时，会创建一个新文件，如果存在同名文件，
#原来的文件会被删除。所以，使用w方式打开文件时应特别小心，避免删除原来有用的文件。
#以w方式打开文件时，只能向文件写入数据，数据按先后顺序写入文件。
myfile=open('d:\\test2.txt','w')#以w方式打开文件
myfile.write('one\n')#将字符串写入文件
myfile.writelines(['1','2','abc'])#将列表写入文件，列表对象必须都是字符串
myfile.close()#关闭文件
myfile=open('d:\\test2.txt')#重新以r方式打开文件
print(myfile.read())#打印从文件读出的数据

#以w+方式打开文件
#w+与w方式的唯一区别是前者除了允许写文件，还可以读文件。

#以a方式打开文件
#以a方式打开文件时，写入的数据添加到文件末尾。
myfile=open('d:\\test.txt','a')#以a方式打开文件
myfile.write('\n123456')#将字符串写入文件
myfile.close()#关闭文件
myfile=open('d:\\test.txt','r')
print(myfile.read())#打印读出的文件内容
myfile.close()#关闭文件

#以a+方式打开文件
#a+与a方式的唯一区别是前者除了允许写入数据，还可以读出文件数据。