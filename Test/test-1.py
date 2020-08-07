# 编写程序，输入一个大于 2 的自然数，然后输出小于该数字的所有素数组成的列表。
# 1、	理解筛选法求解素数的原理。
# 2、	理解列表切片操作。
# 3、	熟练运用内置函数 enumerate()。
# 4、	熟练运用内置函数 filer()。
# 5、	理解序列解包工作原理。
# 6、	初步了解选择结构和循环结构。


def judgment(x):
    flag = 1
    for i in range(2, x - 1):
        if x % i == 0:
            flag = 0
    if flag == 1:
        return x


num = int(input('输入一个大于 2 的自然数:'))
print([i for i in filter(judgment, [i for i in range(num)])])

