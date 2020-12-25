#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 1
# 204113 Sec 001

def eratosthenes(n, show_step=False):
    list_data = list(range(2, n))
    result_list_data = []

    while (list_data <= n):
        if show_step != False:
            a = (list_data[0]%2) != 0
            result_list_data += a
            
        else:
            print('----')
            print(result_list_data)
            

def main():
    result = eratothenes(20, True)     
    print('----') 
    print(result)



if __name__ == '__main__':
    main()