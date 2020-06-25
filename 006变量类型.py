counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

a = b = c = 1

print(counter)
print(miles)
print(name)
print(name[1:3])
print(a)

# Python有五个标准的数据类型：
#
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

print('-------python  数字--------')
# 数字数据类型用于存储数值。
#
# 他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
#
# 当你指定一个值时，Number对象就会被创建

# 类型：int （整型）,long ,float（浮点型）,complex（复数）
# 注意：long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]

tinylist = [123, 'john']

print(list[1:3])
print(tinylist * 2)

# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
#
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])

# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values()) # 输出所有值

# Python数据类型转换
# int() 函数用于将一个字符串或数字转换为整型。
print('------ Python数据类型转换-----')
print(int(3.6))
print(complex(1, 2))