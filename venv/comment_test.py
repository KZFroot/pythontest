# -*-coding:utf-8-*-
# 单行注释
# pyhton是一门弱类型语言 弱类型包含两方面的含义：1 所有的变量无须声明即可使用 或者对从未用过的变量赋值就是声明该变量
# 2变量的数据类型可以随时改变 同一个变量可以一会是数值型 一会是字符串型
"""
多行注释 三个单引 或者三个双引
注释
"""
'''
多行注释
'''
# 这是一个简单的单行注释

# 变量
a = 5
a = "hello world"
# 函数对数据进行有效的处理
if __name__ == '__main__':
    print(a)
    type(a)
    print(type(a))
# print() 的函数可以处理多个变量
user_name = 'Charlie'
user_age = 8
print("读者名：", user_name, "年龄：", user_age)
# print()函数默认空格隔开多个变量，如果读者希望改变默认的分隔符，可以通过sep参数进行设置
print("读者名:", user_name, "年龄:", user_age, sep='?')
# 设置end参数，指定输出之后不在换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
# print(values,sep,end,file,flush )
# file参数指定print()函数的输出目标,默认是标准输出 也就是屏幕 因此print()输出到屏幕上
f = open("poem.txt", "w", encoding="utf-8")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()
# print() 函数的flush参数用于控制输出缓存，该参数一般保持为False 这样子可以获得较好的性能
