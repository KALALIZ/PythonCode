#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 3
# 204111 Sec 001

def is_prime(n, i=2):
    if n==i:
        return True
    elif n%i == 0:
        return False
    else:
        return is_prime(n, i+1)

def main():
    n = int(input("input n: "))
    print(is_prime(n))

if __name__ == '__main__':
    main()