#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 4
# 204111 Sec 001


def main():
    n = int(input(""))
    life_path(n)


def life_path(n):
    first = 0
    total = 0
    while (n > 0):  # หาผลรวมของจำนวณที่รับเข้ามา
        first = n % 10
        n = n // 10
        total += first

    while (total >= 10):  # ทำให้เลขเหลือแค่หลักเดี
        first = total % 10
        total = total // 10
        total += first
    print(total)
    return total


if __name__ == '__main__':
    main()
