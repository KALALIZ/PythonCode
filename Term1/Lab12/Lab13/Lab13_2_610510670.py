#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 13
# Problem 2
# 204111 Sec 001

def power_set(set_a):
    ans_ = [set()]
    for i in set_a:
        for j in ans_:
            ans_ = ans_ + [list(j)+[i]]
            
    x = []
    for i in ans_:
        y = set(i)
        x.append(y)       
    
    return x


