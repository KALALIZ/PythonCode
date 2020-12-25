#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 1
# 204111 Sec 001

def is_anagram(str1, str2):
    word1 = []
    word2 = []

    for i in list(str1.lower()):
        if i.isalpha() == True:
            word1.append(i)

    for i in list(str2.lower()):
        if i.isalpha() == True:
            word2.append(i)

    word1 = sorted(word1)
    word2 = sorted(word2)

    if word1 == word2:
        return True
    else:
        return False

def main():
    str1 = str(input())
    str2 = str(input())
    print(is_anagram(str1, str2))


if __name__ == '__main__':
    main()