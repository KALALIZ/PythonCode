#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 1
# 204113 Sec 001


def string_to_signed_int(x):
    ans = 0
    for i in range(len(x)):
        if i == 0:
            ans += int(x[i]) * -2**(len(x) - (i + 1))
        else:
            ans += int(x[i]) * 2**(len(x) - (i + 1))
    return ans


def main():
    x = input(str)
    print(string_to_signed_int(x))


if __name__ == '__main__':
    main()
