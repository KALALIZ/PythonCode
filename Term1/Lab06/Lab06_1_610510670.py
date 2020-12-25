#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 1
# 204111 Sec 001


def int_power(x, y):
    ans = 1
    if y < 0:
        for i in range(abs(y)):
            ans *= x
        return 1 / (ans)
    else:
        for i in range(y):
            ans *= x
        return ans



def main():
    # รับค่า x, y
    x = float(input("X: "))
    y = int(input("Y: "))

    # คำนวณหาค่าของคำตอบ
    result = int_power(x, y)

    # แสดงผลที่คำนวณได้
    print(result)


if __name__ == "__main__":
    main()
