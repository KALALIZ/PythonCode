#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 03
# Problem 1
# 204111 Sec 001

import math
def find_r_from_surface_area(surface_area):
    r = math.sqrt(surface_area/(4*math.pi))
    return r
def sphere_volume(radius):
    v = (4/3)*math.pi*radius**3
    return v

def main():
    #รับค่าพื้นที่ผิวทรงกลม
    surface = float(input("input surface area: "))

    #คำนวณหาค่า radius
    radius = find_r_from_surface_area(surface)
    
    #นำค่า radius ไปคำนวณหาค่าปริมาตรทรงกลม
    volume = sphere_volume(radius)


    #แสดงผลปริมาตรทรงกลม
    print("volume = %.2f"%sphere_volume(radius))
    







if __name__ == "__main__":
    main()
