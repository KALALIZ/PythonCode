#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 1
# 204111 Sec 001

def love6(first, second):
    if(first == 6) or (second == 6):
        return True
    elif(first + second) == 6:
        return True      
    elif(first - second) == 6 or (second - first) == 6:
        return True      
    else:
        return False
       
    
def main():
    
    #รับค่า first
    first = int(input("Input First Number: "))

    #รับค่า second
    second = int(input("Input Second Number: "))

    #คำนวณค่า Boolean
    result = love6(first, second)

    #แสดงผลคำตอบ
    print(result)
    


    



if __name__ == "__main__":
    main()
