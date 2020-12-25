#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 1
# 204113 Sec 001


def two_power_x(i):
    if i & (i - 1) == 0:
        return 1
    else:
        return 0


def main():
    i = input()
    print(two_power_x(i))


if __name__ == '__main__':
    main()
