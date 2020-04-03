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

"""
多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
"""
total = "item_one" +"\t"+ \
        "item_two" +"\t"+ \
        "item_three"
#print(total)
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total1 = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

#print(total1)

total2 = {'item_one', 'item_two', 'item_three',
        'item_four', 'item_five'}

#print(total2)


total3 = ('item_one', 'item_two', 'item_three',
        'item_four', 'item_five')

#print(total3)


'''
数据类型：python中数字有四种类型：整数、布尔型、浮点数和复数。
    int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    bool (布尔), 如 True。
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

#字符串(String)
#    ①：python中单引号和双引号使用完全相同。
#    ②：使用三引号('''或""")可以指定一个多行字符串。
#    ③：转义符 '\'
#    ④：反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#    ⑤：按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
#    ⑥：字符串可以用 + 运算符连接在一起，用 * 运算符重复。
#    ⑦：Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
#    ⑧：Python中的字符串不能改变。
#    ⑨：Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
#    ⑩：字符串的截取的语法格式如下：变量[头下标:尾下标:步长]


#等待用户输入
'''
import sys #这里实现了空行 下面说空行的作用

print (sys.argv[0])
price =input("price:[eg, 10,20]\n")
a=price.split(',')
print("price:"+price)
'''

"""
空行[空行也是程序代码的一部分]
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
"""


#同一行显示多条语句[语句之间使用分号(;)分割]
#import sys; x = 'python to hello'; sys.stdout.write(x + '\n')  #几条语句写在一行


#代码组 [多个语句构成]
"""
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
"""
import sys

#print (sys.argv[0])
int price=0
price =input("请输入值：")


if (price<10):
    print("我是小于10的数字")
elif (price==10):
    print("我刚好是10") 
else:
    price("我是大于10的数字")