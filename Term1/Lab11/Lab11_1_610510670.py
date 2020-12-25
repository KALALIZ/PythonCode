#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 11
# Problem 1
# 204111 Sec 001

def matrix_mult(m1, m2):
    if len(m1[0]) != len(m2):
        return None

    mtrx_ = [[0] * len(m2[0]) for i in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                mtrx_[i][j] += (m1[i][k]) * (m2[k][j])

    return mtrx_
