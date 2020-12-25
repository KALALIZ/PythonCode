#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 2
# 204111 Sec 001

def classify(list_x):
    list_a_int_ = []
    list_b_float_ = [] 
    list_c_str_ = []

    for i in list_x:
        if isinstance(i,int) == True:
            list_a_int_.append(i)
            
        if isinstance(i,float) == True:
            list_b_float_.append(i)
            
        if isinstance(i,str) == True:
            list_c_str_.append(i)

    return (list_a_int_, list_b_float_, list_c_str_)

