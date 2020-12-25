#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 12
# Problem 2
# 204111 Sec 001


def search_event(list_x, key):
    day_ = dict(list_x)
    ans = []

    for i in key.split("/"):
        x = int(i)
        ans.append(str(x))
    y = "/".join(ans)

    try:
        return (y, day_[y])
    except:
        return None


