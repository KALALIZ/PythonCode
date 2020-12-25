#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 10
# Problem 4
# 204111 Sec 001

def uniform(line):
    cap_ = []
    low_ = []
    ans_ = []
    num_ = []

    for i in list(line):
        if i.isupper() == True:
            cap_.append(i)
        else:
            low_.append(i)

    if len(cap_) < len(low_):
        ans_ = line.lower()
    
    elif len(cap_) > len(low_):
        ans_ = line.upper()
    
    else:
        num_ = list(line).pop(0)
        if num_.isupper() == True:
            ans_ = line.upper()
        else:
            ans_ = line.lower()
        
    return ans_

