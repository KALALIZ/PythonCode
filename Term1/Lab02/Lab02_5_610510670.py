#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 5
# 204111 Sec 001

import math
n = int(input("Enter n: "))                 #รับค่าพจน์ที่ n
GR = (1 + math.sqrt(5))/2                   #สูตรค่าคงที่อัตราส่วนทองคำ
F = (GR**n)/(math.sqrt(5)) + 0.5            #สูตรบิเนต์
print("fib(%d) = %d"%(n,F))
 
