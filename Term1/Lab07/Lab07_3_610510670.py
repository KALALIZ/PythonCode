#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 3
# 204111 Sec 001


def main():
    n = int(input(""))
    triangle(n)


def triangle(n):
    for i in range(n):
        for j in range(n):
            if (i == j):
                print("*", end=" ")
            elif (i == (n - 1)):
                print("*", end=" ")
            elif (j == 0):
                print("*.", end=" ")
            elif (i < j):
                print(" ", end=" ")
            else:
                print(".", end=" ")

        print()


if __name__ == '__main__':
    main()
