#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 12
# Problem 4
# 204111 Sec 001

def polynomial_addition(p1,p2):
    polyn_ = []
    plomb_ = dict()

    for i in p1:
        if i[0] not in plomb_:
            plomb_[i[0]] = i[1]
        elif i[0] in plomb_:
            a = plomb_[i[0]] + i[1]
            plomb_[i[0]] = a
    for i in p2:
        if i[0] not in plomb_:
            plomb_[i[0]] = i[1]
        elif i[0] in plomb_:
            a = plomb_[i[0]] + i[1]
            plomb_[i[0]] = a
    for i in plomb_:
        if plomb_[i] != 0:
            polyn_.append((i,plomb_[i]))
    return sorted(polyn_, reverse=True)