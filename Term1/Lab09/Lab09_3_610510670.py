#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 3
# 204111 Sec 001

def nondest_rotate_list(list_a, n):
    list_1_ = []
    list_2_ = []

    if n == 0:
        print(list_a)
    
    elif n < 0:
        for i in range(abs(n)):
            list_1_ = list_a[:len(list_a) - (len(list_a) - 1)]
            list_2_ = list_a[len(list_a) - (len(list_a) - 1):]
            list_a = list_2_ + list_1_
            
    elif n > 0:
        for i in range(n):
            list_1_ = list_a[len(list_a) - 1:]
            list_2_ = list_a[:len(list_a) - 1]
            list_a = list_1_ + list_2_

    return list_a


