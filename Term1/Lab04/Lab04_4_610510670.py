#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 4
# 204111 Sec 001           

def round_to_int(x):
    if x < 0:
        m = 1    #ให้ 1 = ค่าจำนวนลบ

    else:
        m = 0    #ให้ 0 = ค่าจำนวณบวก


    a = abs(x)   #ทำให้เป็นจำนวณเต็มบวกโดยเก้บค่าไว้ที่ a
    if (a%1 >= 0.5):
        a = int(a) + 1
    else:
        a = int(a)

    if m == 1:
        a = a*(-1)
    return a
            
def main():
    #รับค่าจำนวณจริง x
    x = float(input(""))

    #คำนวณหาค่าจำนวณเต็มจากการปัดเศษ
    ans = round_to_int(x)

    #แสดงผลคำตอบที่ได้
    print(ans)

           
        








if __name__ == "__main__":
    main()
