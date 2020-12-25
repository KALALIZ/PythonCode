#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 2
# 204111 Sec 001


def float_to_bin(x):  #function คิดจำนวนเต็ม
    i = 0
    a = 0
    r = abs(x)//1 #เลขจำนวนเต็ม
    while (r != 0):
        a += (r%2)*(10**i)
        i += 1
        r = r//2
    result = a + decimal(x)
    if x < 0:
        result = result *(-1)
    return result

def decimal(x): #function คิดทศนิยม
    i = -1
    a = abs(x)%1
    c = 0
    while (i >= -6):
        b = a*2
        c += (b//1)*(10**i)
        i -= 1
        a = b%1
    return c


def main():
    # รับค่าเลขฐาน 10
    x = float(input(""))

    # คำนวณแปลงเลขฐาน10เป็นเลขฐาน2
    result = float_to_bin(x)

    # แสดงผลค่าที่คำนวณได้
    print(result)

if __name__ == "__main__":
    main()
