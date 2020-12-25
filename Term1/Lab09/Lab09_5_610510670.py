#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 09
# Problem 5
# 204111 Sec 001


def three_digits_to_word(n):
    
    unit_list_ = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    long_list_ = len(unit_list_)
    ten_list_ = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < long_list_:
        return unit_list_[n]

    pos = 0
    k = n
    while k > 0:
        k = k // 10
        pos += 1

    number_ = ''
    
    if pos == 2:
        (a,b) = divmod(n,10)
        if b == 0:
            number_ = ten_list_[a]
        else:
            number_ = ten_list_[a] + "-" + unit_list_[b]

    elif pos == 3:
        (a,b) = divmod(n,100)
        (c,d) = divmod(b,10)
        
        if b == 11:
            number_ = unit_list_[a] + " " + "hundred" + " " + unit_list_[b]
        elif 11 < b < 20:
            number_ = unit_list_[a] + " " + "hundred" + " " + unit_list_[b]
        elif c == 0:
            number_ = unit_list_[a] + " " + "hundred" + " " + unit_list_[d]
        elif d == 0:
            number_ = unit_list_[a] + " " + "hundred" + " " + ten_list_[c]
        else:
            number_ = unit_list_[a] + " " + "hundred" + " " + ten_list_[c] + "-" + unit_list_[d]

    return number_

def num_to_word(num):

    if num == 0:
        return 'zero'
   
    ans = ''
    (a,b) = divmod(num,1000)
    (c,d) = divmod(a,1000)
    ans = three_digits_to_word(b)
    
   
   
    if d > 0:
        ans = three_digits_to_word(d) + " " + "thousand" + " " + ans
      
    (e,f) = divmod(c,1000)

    if f > 0:
        ans = three_digits_to_word(f) + " " + "million" + " " + ans
        
    (g,h) = divmod(e,1000)

    if h > 0:
        ans = three_digits_to_word(h) + " " + "billion" + " " + ans
      
    return ans

