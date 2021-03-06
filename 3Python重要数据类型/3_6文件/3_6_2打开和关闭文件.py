#open()函数用于打开文件，并创建一个文件对象。
#open()函数基本格式为：
#myfile = open(filename[,mode])
# 其中，myfile为引用文件对象的变量，
# filename为文件名字符串，
# mode为文件读写模式。

#文件读写模式有如下几种：
#w：写文件，创建新文件。若文件已存在，原来的文件被覆盖。
#a：以追加方式写文件。若文件存在，写入的数据默认添加到文件末尾。文件不
#存在时会创建新文件。
#r：读文件，省略文件读写模式时，默认为读文件。
#b：组合使用（wb、ab、rb），表示读写二进制文件，未使用时读写文本文件。
#+：用在模式末尾，表示打开文件后可同时进行读、写操作。例如：w+、r+。

#close()方法用于关闭文件。
# 通常，Python会使用内存缓冲区缓存文件数据。
# 关闭文件时，Python可将缓冲的数据写入文件，然后关闭文件，
# 释放对文件的引用。当然，Python可自动关闭未使用的文件。
#myfile.close()#关闭文件
#myfile.flush()#flush方法可将缓冲区内容写入文件，但不关闭文件


