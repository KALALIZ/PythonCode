#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 1
# 204111 Sec 001


def gcd(x, y):
    if y == 0:  #base case
        return x
    else:
        return gcd(y, x % y)    #divide & conquer


def main():
    x = int(input(""))
    y = int(input(""))
    print(gcd(x, y))

if __name__ == "__main__":
    main()
