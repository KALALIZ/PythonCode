#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 13
# Problem 3
# 204111 Sec 001

import string

def word_count(text):
    
    char_ = ((text.strip(string.punctuation)).lower()).split()
    x = {}
    alp_ = string.punctuation

    for i in char_:
        word_ = i.strip(alp_)
        if word_ in x:
            x[word_] += 1
        else:
            x.update({word_:1})

    return x
