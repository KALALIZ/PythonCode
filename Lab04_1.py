import math


class Circle(object):

    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)


class Rectangle(object):

    def __init__(self, w, h):
        self.width = w
        self.hight = h

    def perimeter(self):
        return (self.width * 2) + (self.hight * 2)

    def area(self):
        return self.width * self.hight


def main():
    info = input()
    info = info.split(' ')
    if info[0] == 'c':
        c = Circle(float(info[1]))
        p = c.perimeter()
        a = c.area()
        print("Circle perimeter is %.2f" % p)
        print("Circle area is %.2f" % a)
    else:
        r = Rectangle(float(info[1]), float(info[2]))
        p = r.perimeter()
        a = r.area()
        print("Rectangle perimeter is %.2f" % p)
        print("Rectangle area is %.2f" % a)

if __name__ == '__main__':
    main()
