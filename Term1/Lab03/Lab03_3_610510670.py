#!/usr/bin/env python3
# ศิลาลักาณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 3
# 204111 Sec 001


def find_square_area(x):
    sq = x**2
    return sq
def find_triangle_area(x):
    tr = (1/2)*(x/3)*(x/3)
    return tr
def octagon_area(x):
    oc = (x**2) - 4*((1/2)*(x/3)*(x/3))
    return oc

def main():
    #รับค่าความยาวด้านรูปสี่เหลี่ยม
    length = float(input("Input length: "))

    #คำนวณหาพื้นที่รูปสี่เหลี่ยม
    square = find_square_area(length)
    

    #คำนวณหาพื้นที่รูปสามเหลี่ยม
    triangle = find_triangle_area(length)

    #คำนวณหาพื้นที่รูปแปดเหลี่ยม
    octagon = octagon_area(length)
    

    #แสดงผลค่าพื้นที่รูปแปดเหลี่ยม
    print("octagon area is: %.6f"%octagon_area(length))
   







if __name__ == "__main__":
    main()

