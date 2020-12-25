#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 3
# 204111 Sec 001

print("First Equation")                     
m1 = float(input("Input m1: "))             #รับค่าความชันที่ 1
b1 = float(input("Input b1: "))             #รับค่าb1                            
print("Second Equation")                    
m2 = float(input("Input m2: "))             #รับค่าความชันที่ 2
b2 = float(input("Input b2: "))             #รับค่าb2
x = (b2-b1)/(m1-m2)
y = m1*x + b1
print("The point of intersection is at x = %.2f and y = %.2f"%(x,y))
