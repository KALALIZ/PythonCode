#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 2
# 204111 Sec 001

# ขออนุญาตไม่ใส่ main ค่ะ grader ไม่ผ่าน หนูแก้ไม่ได้ค่ะ

def n_base_to_10(n, num, i=0):
    if num == 0:    #base case
        return 0
    x = num%10  #เก็บค่าเลขทีละตัว
    y = n_base_to_10(n, num//10, i+1)
    return y + (x*(n**i))   #นำเลขมารวมค่าใหม่

    


    
        
