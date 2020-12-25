#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 13
# Problem 4
# 204111 Sec 001


def square_matrix(list_x):
    mtrx_ = []
    for i in list_x:
        mtrx_.append(len(i))
    col_ = max(mtrx_)
    row_ = len(list_x)
    x = max(col_, row_)

    zero_ = [[0] * x for j in range(x)]

    a = 0
    b = 0
    for j in range(len(list_x)):
        while b < len(list_x[a]):
            zero_[a][b] += list_x[a][b]
            b += 1
        if b > len(list_x[a]) - 1:
            b = 0
            a += 1
    list_x.clear()
    list_x.extend(zero_)
