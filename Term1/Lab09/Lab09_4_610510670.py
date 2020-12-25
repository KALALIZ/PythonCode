#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 4
# 204111 Sec 001


def dest_rotate_list(list_a, n):
    list_ = []

    if n < 0:
        for i in range(abs(n)):
            list_ = list_a.pop(0)
            list_a.insert(len(list_a), list_)

    elif n >= 0:
        for i in range(n):
            list_ = list_a.pop(-1)
            list_a.insert(0, list_)
