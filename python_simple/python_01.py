# :但行注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
#第一个hello world
#print("hello word");  #这里不要分号也是可以的 

'''
Python 标识符:
    在 Python 里，标识符由字母、数字、下划线组成。
    在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
    Python 中的标识符是区分大小写的。  
    以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
    以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
Python 可以同一行显示多条语句，方法是用分号 ; 分开
'''
#print ('hello');print ('python');

'''
    Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
'''

# 正确的缩进
"""
if True:
    print ("True")
else:
    print ("False")
"""

#错误的缩进一
"""
if True:
    print ("Answer")
    print ("True")
else:
        print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
"""
#报错信息为：IndentationError: unindent does not match any outer indentation level 
#原因 ：使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可

#错误的缩进二
"""
  print("to hello")  #两个空格的空位
    print ("False")  #一个制表符的空位
"""
#报错信息为：IndentationError: unexpected indent 
#原因 ：tab和空格没对齐的问题
#Python 的代码块中必须使用相同数目的行首缩进空格数。建议每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用

print("to hello")
