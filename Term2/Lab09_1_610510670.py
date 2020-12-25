#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 1
# 204113 Sec 001


import time
import datetime
import matplotlib.pyplot as plt


def rand_float(n):
    x = (int)(time.time()) #initial value of seed
    y = datetime.datetime.now()
    m = (int)(y.microsecond) #modulo m
    a = (int)(y.minute*y.second) #parameter a
    c = (int)(y.minute)
    result = []

    seed = x
    print(x, a, c, m)
    for i in range(n):
        xi = (a*x + c) % m
        result.append(xi/m)
        x = xi
    return result
#--------------------------------------------------------#
def plot(lst):
    colors = 'blue'
    area = 10
    x = [i for i in range(len(lst))]
    plt.scatter(x, lst, s=area, c=colors, alpha=0.5)
    plt.title('Random Number')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    result = rand_float(100)
    plot(result)
    

if __name__ == '__main__':
    main()

