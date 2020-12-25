#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 1
# 204111 Sec 001

F = float(input("Input temperature in Fahrenheit: "))           #รับข้อมูลเป็นองศาฟาเรนไฮต์                                    
C = (F-32)*5/9                                                  #แปลงค่าเป็นองศาเซลเซียส
print("%.2f degree Fahrenheit is %.2f degree Celsius"%(F,C))
