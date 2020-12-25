#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 11
# Problem 2
# 204111 Sec 001

import copy

def remove_row_col(list_a, row, col):
    det_ = copy.deepcopy(list_a)

    try:
        det_.remove(list_a[row])
    except:
        pass
    
    for i in range(len(det_)):
        try:
            det_[i].pop(col)

        except:
            pass

    return det_
