# 整形 定义变量a 赋值56
a = 56
b = 999999999.0

# 以0x或0X开头的整型数值是十六进制形式的整数
hex_value1 = 0x13
hex_value2 = 0Xaf
# 以0b或0B开头的整型数值是二进制


if __name__ == '__main__':
    print(a)
    print(b)
    # type()用于返回变量的类型
    print(type(a))
    print(type(b))
    # 进制形式的数
    print("hex_value1的值为：", hex_value1)
    print("hex_value2的值为：", hex_value2)
