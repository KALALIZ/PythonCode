#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 3
# 204111 Sec 001

def factorize(x):
    print("%d is "%x , end="")
    a = 2
    is_prime = True
    while ((x**0.5) >= a):
        if x%a == 0:
            print(a , " * " , end="")
            is_prime = False
            x = x//a
        else:
            a += 1

    if (is_prime == True):
        print("prime")
    else:
        print(x)
        

def main():
    #รับค่าเลขที่ต้องการแยกตัวประกอบ
    x = int(input(""))

    #แสดงผลที่คำนวณได้จาก function
    factorize(x)


if __name__ == '__main__':
    main()



