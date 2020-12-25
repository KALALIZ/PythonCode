#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 4
# 204111 Sec 001


def reverse_digits(x):
    for i in range(x==0):
        o = x%10
        o = o*(10**i)
        rev = reverse_digits(x//10)
    return rev


    
def main():

    #รับค่าจำนวนเต็มบวก
    x = int(input("input numbers: "))


    #กลับหลักจำนวน
    reverse = reverse_digits(x)



    #แสดงผลจำนวนที่กลับหลักแล้ว
    print("output: %d"%reverse)






if __name__ == "__main__":
    main()

   