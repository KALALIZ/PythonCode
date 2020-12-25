#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 5
# 204111 Sec 001

def nearest_odd(x):    
    a = x//1                #แปลงค่าที่เป็นทศนิยมให้เป็นจำนวนเต็มโดยเก็บค่าไว้ที่ a
    if a%2 == 0:            #ถ้า a เป็นจำนวนคู่
        ans = int(a+1)
    else:
        ans = int(a)
    return ans

def main():
    #รับค่าจำนวณจริง
    x = float(input(""))

    #คำนวณค่าที่ใกล้เคียงกับจำนวรที่รับเข้ามา
    ans = nearest_odd(x)

    #แสดงผลค่าที่ได้
    print(ans)


if __name__ == "__main__":
    main()


    
       
                
    
        
    

    
    

