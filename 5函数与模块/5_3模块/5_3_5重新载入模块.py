#再次使用import和from导入模块时，
#其本意通常是重新执行模块代码，
#恢复相关变量到模块执行时的状态。
#显然，这种愿望通过再次使用import和from导入是无法达到的。

#Python在imp模块中提供了reload函数来重新载入并执行模块代码。
#使用reload重载模块时，如果模块文件已经被修改，则会执行修改后的代码。
from importlib import reload#导入reload函数
#reload(math)#重新加载模块，模块代码被再次执行