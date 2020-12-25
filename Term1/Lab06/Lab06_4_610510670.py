#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 06
# Problem 4
# 204111 Sec 001


total_student = int(input("Total students: "))
print("Enter score: ")
i = 0
Max = 0 
Runner = 0
total = 0
avg = 0
while i < total_student:
    score = int(input(""))
    i += 1
    if score > Max:
        Runner = Max
        Max = score
    elif score < Max and score > Runner:
        Runner = score
    total += score
   

avg = total/total_student

print("---")
print("Max score is: %.2f" % Max)
if Runner == 0:
    print("Runner up is: None")
else:
    print("Runner up is: %.2f" % Runner)
print("Average is: %.2f" % avg)
