#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 5
# 204111 Sec 001

def kth_digit(number,k):
    nb = abs(number % (10**(k+1)) // (10**k))
    return nb

def set_kth_digit(number, k, value):
    res = number - (kth_digit(number, k)*(10**k))+(value*(10**k))
    return res


    
def main():
    #รับค่าจำนวนเต็ม
    number = int(input("input number: "))

    #รับค่าหลักที่ต้องการเปลี่ยนค่า
    k = int(input("input k: "))

    #รับค่าเลขที่ต้องการเปลี่ยน
    value = int(input("input value: "))

    #เปลี่ยนเลขเป็นค่าที่ต้องการ
    print("output is: %d"%set_kth_digit(number, k, value))

    
    




if __name__ == "__main()___":
    main()
