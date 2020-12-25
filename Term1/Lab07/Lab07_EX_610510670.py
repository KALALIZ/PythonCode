#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Extra
# 204111 Sec 001



def pyramid_stairs(n):
    som = n - 2
    slk = n - 1
    if (n != 0):
        print(" "*((slk)*5)+"  o  ************  o ")
    sllk = 1
    for i in range(n):
        print(" "*(5*(slk)) + " /|\ *" + " "*(i*10) + "          * /|\ ")
        print(" "*(5*(slk)) + " / \ *" + " "*(i*10) + "          * / \ ")
        if(i < n-1):
            print(" "*(5*som) + "  o  ******" + " "*((sllk)*10) + "******  o")
        else:
            print("******" + "*"*(n*10) + "******")
        sllk += 1
        som -= 1
        slk -= 1

def main():
    n = int(input())
    pyramid_stairs(n)

if __name__ == '__main__':
    main()

