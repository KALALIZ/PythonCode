#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 2
# 204111 Sec 001

def my_max_mid_min(a, b, c):
    if (a >= b) and (a > c):    #กรณี a > b > c 
        if b > c:                                   
            print("max = %d \n  mid = %d \n min = %d"%(a,b,c))
        else:                   #กรณีถ้า a > c > b
            print("max = %d \n  mid = %d \n min = %d"%(a,c,b))
                    

    elif (b > a) and (b > c):   #กรณี b > a > c
        if a > c:                                   
            print("max = %d \n mid = %d \n min = %d"%(b,a,c))
        else:                   #กรณีถ้า b > c > a
            print("max = %d \n mid = %d \n min = %d"%(b,c,a))
    else :                      #กรณี c > a > b
        if a > b:
            print("max = %d \n mid = %d \n min = %d"%(c,a,b))
        else:                   #กรณีถ้า c > b > a
            print("max = %d \n mid = %d \n min = %d"%(c,b,a))
    


    
def main():
    #รับค่าจำนวณ a
    a = int(input("Input A: "))

    #รับค่าจำนวณ b
    b = int(input("Input B: "))

    #รับค่าจำนวณ c
    c = int(input("Input C: "))

    #แสดงผลค่าที่คำนวณได้
    my_max_mid_min(a, b, c)
                  










if __name__ == "__main__":
    main()



