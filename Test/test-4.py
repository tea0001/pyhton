# 编写程序，实现磁盘垃圾文件清理功能。
# 要求程序运行时，通过命令行参数指定要清理的文件夹，然后删除该文件夹及其子文件夹中所有扩展名为tmp、log、obj、txt以及大小为0的文件
# 1、	熟练运用标准库os和os.path中的函数。
# 2、	理解sys库中argv成员用法。(外部调用时输入的参数列表，第一个为程序本身，后面的为参数列表)
# 3、	理解Python程序接收命令行参数的方式。
# 4、	理解递归遍历目录树的原理。
# 5、	了解从命令提示符环境运行Python程序的方式。
import os
import sys

file_type = ['.tmp', '.log', '.obj', '.txt']


def del_file(file_path):
    if not os.path.isdir(file_path):
        return
    for filename in os.listdir(file_path):
        temp = os.path.join(file_path, filename)
        if os.path.isdir(temp):
            del_file(temp)
        elif os.path.splitext(temp)[1] in file_type or os.path.getsize(temp) == 0:
            os.remove(temp)
            print(temp, '已经被删除')


if __name__ == '__main__':
    file_path = 'C:\\Users\\22395\\Desktop\\python\\Test\\测试'
    # file_path = sys.argv[1]
    del_file(file_path)
