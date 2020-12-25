#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 11
# Problem 4
# 204111 Sec 001

import copy

def sum_nested_list(list_a):

    list_x = copy.deepcopy(list_a)

    sum_ = []
    for i in list_x:
        if isinstance(i,list) == True:
            list_x.extend(i)
        else:
            sum_.append(i)

    x = 0
    for j in sum_:     
        x += j

    return x
