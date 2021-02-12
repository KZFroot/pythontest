# msg = input("请输入你的值：")
# print(type(msg))

if __name__ == '__main__':
    # print(msg)

    s2 = '''The quick brown fox jumps over the lazy dog'''
    print(s2)

    # 原始字符串
r1 = r'D:\pythontest\venv\input_test.py'
print(r1)
# 原始字符串包含的引号,同样需要转义
s3 = r'"Let\'s go",said Charlie'
print(s3)
s4 = r'GOOD MORNING' '\\'
print(s4)

# 字节串(bytes)  字节串由多个字节组成 以字节为单位进行操作 bytes也是不可变序列
# bytes对象只负责以字节(二进制格式)数据，因此bytes对象可用于在网络上传输数据，也可用于存储各种二进制格式的文件 图片 音乐等文件
# 调用bytes()函数(其实是bytes的构造方法)将字符串按指定字符集转换成字节串 如果不指定字符集  默认UTF-8字符集
b1 = bytes()
# 创建一个空的bytes值
b2 = b''
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
# 调用bytes()方法将字符串转换w为bytes对象
b4 = bytes('python就是一个迷', encoding='utf-8')
print(b4)
# 利用字符串的encode()方法编码成bytes,默认使用UTF-8字符集
b5 = "学习python 从头来".encode('utf-8')
print(b5)
# 将bytes对象解码成字符串 默认使用utf-8进行解码
st=b5.decode('utf-8')
print(st)

