#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 13
# Problem 1
# 204111 Sec 001

def count_segment(list_a):

    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0      
    
    for i in list_a:
        
        if i[0] >= 0 and i[1] >= 0:     #Q1
            Q1 += 1
            if i[2] > i[0]:
                Q2 += 1
            if i[2] > i[1]:
                Q4 += 1
            

                
        elif i[0] < 0 and i[1] >= 0:   #Q2
            Q2 += 1
            if i[2] > abs(i[0]):
                Q1 += 1
            if i[2] > i[1]:
                Q3 += 1
            

        
        elif i[0] < 0 and i[1] < 0:   #Q3
            Q3 += 1
            if i[2] > abs(i[0]):
                Q4 += 1
            if i[2] > abs(i[1]):
                Q2 += 1
            


        elif i[0] >= 0 and i[1] < 0:   #Q4
            Q4 += 1
            if i[2] > i[0]:
                Q3 += 1
            if i[2] > abs(i[1]):
                Q1 += 1

    for k in range(len(list_a)):
        x = list_a[k][0]
        y = list_a[k][1]
        r = list_a[k][2]
        if x >= 0 and y >= 0:     #Q1
            if (x**2) + (y**2) < (r**2):
                Q3 += 1
                
        elif x < 0 and y >= 0:   #Q2
            if (x**2) + (y**2) < (r**2):
                Q4 += 1
                
        elif x < 0 and y < 0:   #Q3
            if (x**2) + (y**2) < (r**2):
                Q1 += 1
                
        elif x >= 0 and y < 0:   #Q4
            if (x**2) + (y**2) < (r**2):
                Q2 += 1


    return (Q1,Q2,Q3,Q4)