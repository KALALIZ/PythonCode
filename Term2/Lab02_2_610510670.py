#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 2
# 204113 Sec 001


def two_complement(x):
    a = len(x) - 1
    list_x = list(x)
    num_ = -(int(list_x[0]) * (2 ** a))
    list_x.pop(0)
    a = a - 1
    num_1 = 0
    for i in list_x:
        i = int(i)
        num_1 = num_1 + (i * (2 ** a))
        a = a - 1
    ans = num_ + num_1
    a_1 = x.rfind("1")
    list_x_1 = list(x)
    for i in range(a_1):
        if (list_x_1[i] == "1"):
            list_x_1.insert(i, "0")
            list_x_1.pop(i + 1)
        elif (list_x_1[i] == "0"):
            list_x_1.insert(i, "1")
            list_x_1.pop(i + 1)
    name_ = ""
    for j in list_x_1:
        name_ = name_ + j
    if (name_ == x):
        ans = ans
    else:
        ans = -1 * ans
    return (name_, ans)


def main():
    x = input(str)
    print(two_complement(x))


if __name__ == '__main__':
    main()
