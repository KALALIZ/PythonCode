#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 5
# 204111 Sec 001

def  longest_digit_run(n):
    Max = 0             
    Count = 1           #จำนวนตัวเลขที่ซ้ำ
    while (n > 0):
        First = n%10        #เลขเปรียบเทียบตัวแรก เริ่มจากหลังสุด
        Next = (n//10)%10   #เลขเปรียบเทียบตัวที่สอง ตัวถัดจาก First
        if (First != Next):
            Count = 1
        else:
            Count += 1
        if (Count > Max):
            Max = Count

        n = n//10
    return Max

def main():
    # รับค่าเลขจำนวณหนึ่ง
    n = int(input(""))

    # คำนวณหาจำนวณของตัวเลขซ้ำ
    result = longest_digit_run(n)

    # แสดงผลที่คำนวณได้
    print(result)


if __name__ == "__main__":
    main()
