old = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 年龄月
high = [0.49, 0.50, 0.52, 0.54, 0.56, 0.58, 0.61, 0.64, 0.67, 0.71, 0.75, 0.79]  # 身高米
dic = dict(zip(old,high))
print(dic)


def my_sum(n):
    if n != 1:
        my_sum(n-1)
        return n+my_sum(n-1)
    elif n == 1:
        return 1

if __name__ == '__main__':
    print(my_sum(5))