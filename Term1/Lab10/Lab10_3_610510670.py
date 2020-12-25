#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 10
# Problem 3
# 204111 Sec 001


'''def patterned_message(message, pattern):
    mes_ = str(message)
    pat_ = str(pattern)
    magic_ = mes_.replace(" ", "")
    x = 0

    for i in pat_:
        if i == '*':
            print(magic_[n], end="")
            x += 1
            if x > len(magic_) - 1:
                x = 0
            continue
        elif i == i.isspace():
            print(end=" ")
        elif i == '\n':
            print(end="\n")'''


def patterned_message(message, pattern):
    m = str(message)
    t = str(pattern)
    hello = m.replace(" ", "")
    n = 0

    for i in t:
        if i == '*':
            print(hello[n], end="")
            n += 1
            if n > len(hello) - 1:
                n = 0
            continue
        elif i == i.isspace():
            print(end=" ")
        elif i == '\n':
            print(end="\n")
