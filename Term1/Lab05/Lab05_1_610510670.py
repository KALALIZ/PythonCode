#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 05
# Problem 1
# 204111 Sec 001

import math
def intersects(x1, y1, r1, x2, y2, r2, epsilon=10**-6):
        distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if distance == (r1 + r2):
        return 0
    elif distance > (r1 + r2):
        return -1
    else:
        if abs(distance - (r1 + r2)) > 10**-6:
            return 1
        else:
            return 0

    

    

def main():
        #รับค่า x1, y1, r1, x2, y2, r2
    x1 = float(input("x1: "))  
    y1 = float(input("y1: "))  
    r1 = float(input("r1: ")) 
    x2 = float(input("x2: "))  
    y2 = float(input("y2: "))  
    r2 = float(input("r2: "))
        
        #คำนวณหาค่าระยะของวงกลมทั้งสองวง
    result = intersects(x1, y1, r1, x2, y2, r2, epsilon=10**-6)

        #แสดงผลว่าวงกลมทั้งสองตัดกัน สัมผัสกัน หรือไม่ตัดกัน
    print(result)




if __name__ == "__main__":
    main()
