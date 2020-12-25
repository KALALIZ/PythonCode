#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 2
# 204111 Sec 001

H = float(input("Input height (m): "))        #รับข้อมูลความสูง มีหน่วยเป็น เมตรยกกำลังสอง
W = float(input("Input weight (kg): "))       #รับข้อมูลน้ำหนัก มีหน่วยเป็น กิโลกรัม
BMI = W/(H*H)                                 #คำนวณหาค่าดัชนีมวลกาย  
print("BMI is %.4f"%BMI)
    
