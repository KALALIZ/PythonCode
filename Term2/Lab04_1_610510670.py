#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 1
# 204113 Sec 001

import math


class Circle(object):

    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)

    def print(self):
        print("Circle perimeter is %.2f" % self.perimeter())
        print("Circle area is %.2f" % self.area())


class Rectangle(object):

    def __init__(self, w, h):
        self.width = w
        self.hight = h

    def perimeter(self):
        return (self.width * 2) + (self.hight * 2)

    def area(self):
        return self.width * self.hight

    def print(self):
        print("Rectangle perimeter is %.2f" % self.perimeter())
        print("Rectangle area is %.2f" % self.area())




def main():
    info = input()
    info = info.split(" ")
    if info[0] == "c":
        c = Circle(float(info[1]))
        c.print()
    else:
        r = Rectangle(float(info[1]), float(info[2]))
        r.print()

if __name__ == '__main__':
    main()
