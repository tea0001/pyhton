# 编写程序模拟猜数游戏。程序运行时，系统生成一个随机数，然后提示用户进行猜测，并根据用户输入进行必要的提示（猜对了、太大了、太小了）
# 如果猜对则提前结束程序，如果次数用完仍没有猜对，提示游戏结束并给出正确答案。
# 1、	熟练运用选择结构与循环结构解决实际问题。
# 2、	注意选择结构嵌套时代码的缩进与对齐。
# 3、	理解带 else 子句的循环结构执行流程。
# 4、	理解条件表达式 value1 if condition else value2 的用法。
# 5、	理解使用异常处理结构约束用户输入的用法。
# 6、	理解带 else 子句的异常处理结构的执行流程。
import random

number = random.randint(0, 10)
print('猜数游戏即将开始')
times = 5
while times != 0:
    user_number = int(input('请输入您猜的（0-10）数字:'))
    if user_number < number:
        print('太小了')
    elif user_number > number:
        print('太大了')
    else:
        print('猜对了，你是我肚子里的蛔虫吗？')
        break
    times -= 1
if times == 0:
    print('很遗憾，游戏结束!  正确答案是%d' % number)