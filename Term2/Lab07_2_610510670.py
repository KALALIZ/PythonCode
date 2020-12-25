#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 07
# Problem 2
# 204113 Sec 001

'''class find_largest_number(object):

    def __init__(self, text):
        self.text = text'''


def largest_number(text):
    text_ = text.split()
    number_of_text = []
    large_number = []
    found_number = '0123456789,'
    for i in range(len(text_)):
        if len(text_) in found_number:
            number_of_text = len(text_)
            return number_of_text
        else:
            return 

def insertion_sort(number_of_text):
    size = len(number_of_text)
    a = number_of_text[:]

    for i in range(1, size):
        j = i
        while j > 0and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a


def main():
    text = str(input())
    print(largest_number(text))

if __name__ == '__main__':
    main()