counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

a = b = c = 1

print(counter)
print(miles)
print(name)
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