# 定义一个三维向量类，并定义相应的特殊方法实现两个该类对象之间的加、减运算（要求支持运算符+、-），
# 实现该类对象与标量的乘、除运算（要求支持运算符*、/），以及向量长度的计算（要求使用属性实现）
# 1、	了解如何定义一个类。
# 2、	了解如何定义类的私有数据成员和成员方法。
# 3、	了解如何使用自定义类实例化对象。
from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __get(self):
        return self.__x, self.__y, self.__z

    def add(self, v):
        if isinstance(v, Vector):
            return self.__x + v.__x, self.__y + v.__y, self.__z + v.__z
        else:
            print('不能进行加法运算')

    def subtraction(self, v):
        if isinstance(v, Vector):
            return self.__x - v.__x, self.__y - v.__y, self.__z - v.__z
        else:
            print('不能进行减法运算')

    def multiplication(self, v):
        if isinstance(v, int):
            return self.__x * v, self.__y * v, self.__z * v
        else:
            print('不能进行乘法运算')

    def division(self, v):
        if isinstance(v, int):
            return self.__x / v, self.__y / v, self.__z / v
        else:
            print('不能进行除法运算')

    def ChangDu(self):
        return sqrt(sum(i ** 2 for i in [self.__x, self.__y, self.__z]))


if __name__ == '__main__':
    vector1 = Vector(2, 2, 2)
    vector2 = Vector(3, 4, 0)
    print(vector1.add(vector2))
    print(vector1.subtraction(vector2))
    print(vector1.multiplication(3))
    print(vector1.division(2))
    print(vector2.ChangDu())