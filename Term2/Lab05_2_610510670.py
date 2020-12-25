#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 05
# Problem 2
# 204113 Sec 001


def vowelCount(word):
    word_ = list(word)
    vowel_ = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if word == []:
        return 0
    elif word_[0] in vowel_:
        return 1 + vowelCount(word_[1:])
    else:
        return 0 + vowelCount(word_[1:])


def main():
    print(vowelCount("happy birthday"))
    print(vowelCount("Recursive function"))
    print(vowelCount("Puzzle Game"))
    print(vowelCount("Anthony"))
    print(vowelCount("silalak670"))
    print(vowelCount("Let me cater to you. Cause baby this is your day. Do anything for my man. Baby you blow me away"))
    print(vowelCount("PUT YOUR HANDS UP!!!!!"))
    print(vowelCount(" "))
    print(vowelCount("AEIOU"))
    print(vowelCount("prayutjaaaaa"))


if __name__ == '__main__':
    main()
