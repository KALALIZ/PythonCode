#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 2
# 204111 Sec 001


def main():
    # รับค่าจำนวณ
    x = int(input(""))
    # รับค่าฐานของจำนวณ
    base = input()
    if base == "":
        digit_count(x) #กรณีไม่ใส่baseมา ถือว่าเป็นฐาน10
    else:
        base = int(base)
        digit_count(x, base=10)

    result = digit_count(x, base=10)
    print(result)


def digit_count(x):

    if (base == 10):
        a = 1
        r = x
        while (x % 10 == 0):
            a += x % 10
            r += r//10
            a += 1.

        return a
    
    else:
        i = 0
        a = 0
        r = abs(x) // 1  # เลขจำนวนเต็ม
        while (r != 0):
            a += (r % 2) * (10**i)
            i += 1
            r = r // 2
        return a


if __name__ == '__main__':
    main()
