#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 2
# 204111 Sec 001

def reverse_digits(x):
    o = x % 10
    t = (x//10)%10
    th = (x//100)%10
    f = (x//1000)%10
    rev = (o*10**3)+(t*10**2)+(th*10**1)+(f*10**0)
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
