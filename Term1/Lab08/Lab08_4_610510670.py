#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 4
# 204111 Sec 001

def series(n):
    if n<=1:
        return n
    elif n%2 == 1:
        return series(n+1, )
    else:
        return series(n-1, )



def main():
    n = int(input(""))
    print(series(n))

if __name__ == "__main__":
    main()