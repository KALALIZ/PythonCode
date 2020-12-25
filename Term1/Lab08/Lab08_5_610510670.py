#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 5
# 204111 Sec 001


def reverse_num(num):
    a = num
    i = 0
    while a > 0:
        a = a // 10
        i += 1

    if num == 0:
        return 0
    x = num % 10
    y = reverse_num(num // 10)
    return y + (x * (10**(i - 1)))
