#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 1
# 204111 Sec 001

def main():   
    x = int(input(""))
    y = int(input(""))
    result = sum_prime_in_range(x, y)
    print(result)


def sum_prime_in_range(x, y):   
    total = 0
    
    for x in range(x, y, 1):
        if (x%2 != 1):
        if (x%2 == 1): 
            total += x  
        elif (x == 2):
            total += x      

    return total

    
    
            
        

            
        
if __name__ == '__main__':
    main()