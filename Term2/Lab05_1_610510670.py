#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 05
# Problem 1
# 204113 Sec 001


def linear_search(key, l):
    for i in range(len(list(l))):
        if key == l[i]:
            return i
        else:
            return None
                



def main():
    assert(linear_search(3, [1, 2, 3, 4, 5]==2))
    assert(linear_search("D", ["A", "B", "C", "D", "E"]==3))
    assert(linear_search(3.1, [1.0, 2.1, 3.0, 3.1, 4]==3))


if __name__ == '__main__':
    main()
