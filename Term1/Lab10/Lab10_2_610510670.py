#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 10
# Problem 2
# 204111 Sec 001


def is_palindrome(x, b):
    if abs(x) > 0:
        n = 1
    else:
        n = -1

    first_ = x % 1
    second_ = x - (x % 1)
    x = 0
    y = 0
    num_ = 0

    while second_ > 0:
        a = second_ % b
        second_ = second_ // b
        x += (a * (10 ** num_))
        num_ += 1

    for i in range(6):
        c = first_ * b
        d = c // 1
        first_ *= b - d
        y += (d * (10**(-(i + 1))))

    last_ = str(int((x + y) * n))
    ans_1 = list(last_)
    ans_2 = list(reversed(last_))

    if ans_1 == ans_2:
        return True
    else:
        return False
