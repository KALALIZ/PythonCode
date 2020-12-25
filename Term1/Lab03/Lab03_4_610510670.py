#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 4
# 204111 Sec 001

def kth_digit(number, k):
    nb = (abs((number)//(10**k))%10)
    return nb
    

def main():
    #รับค่าจำนวนเต็ม
    number = int(input("input number: "))

    #รับค่าหลักที่ต้องการคืนค่า
    k = int(input("input k: "))

    #คืนค่าจำนวน
    result = kth_digit(number, k)

    #แสดงผลจำนวนที่ถูกคืนค่าแล้ว
    print(result)
    
    
    


if __name__ == "__main__":
    main()
