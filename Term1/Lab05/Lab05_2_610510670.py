#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# Lab 05
# Problem 2
# 204111 Sec 001

import math
def main():
    #รับค่าความยาวด้าน a
    a = int(input("Input A: "))

    #รับค่าความยาวด้าน b
    b = int(input("Input B: "))

    #รับค่าความยาวด้าน c
    c = int(input("Input C: "))

    #คำนวณหาค่า Boolean
    result = is_p_triple(a, b, c)

    #แสดงผลคำตอบที่ได้
    print(result)


def is_p_triple(a, b, c):
    if a == math.sqrt((b**2)+(c**2)):
        return True
    elif b == math.sqrt((a**2)+(c**2)):
        return True
    elif c == math.sqrt((a**2)+(b**2)):
        return True
    else:
        return False





if __name__ == '__main__':
    main()
    
