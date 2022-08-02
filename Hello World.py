
'''
# print（）函数 输出字符串要加引号 ，数字
# 可以输出中文
print('Hello World!')
print('Hello\nWorld!2') # 转义字符
print('ABC\tB') # 最多4个空格，若有三个已经占用了就只打印一个空格了 要理解含义
print('hello\rworld')# world会覆盖掉hello
#原始的机械打印，回车+换行是两个动作，回车是将光标回到行首，换行是移到下一行，只回车不换行继续打印就把后面的覆盖了
#也就是键盘上的backspace
print('hello\bworld') # o消失了 被覆盖了
print(520)
print(99.33)
print("你好，世界！")
print(1+1)
print(++1)  #不支持++??
'''  #三个单引号 或双引号表示注释


print('http:\\\\www.baidu.com')
#输出双斜线
print("老师说：\"大家好\" ")
#表示双引号
#元字符 使这一行里面转义字符不起作用
print('A\nB')

print(r'A\nB') # 最后一个字符不能是\ 不然报错
# 输出不换行
#print(‘2021’,'开始','学习Python')
print('2021','开始','学习Python')

# 输出数字到文件里面

fp=open('D:/text.txt','a+')  # a+是追加 不会覆盖原来的数据
print('hello world!',file=fp) # 注意这里要写 file= !!!!11
fp.close()