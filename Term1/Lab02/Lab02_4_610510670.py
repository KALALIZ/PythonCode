#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 02
# Problem 4
# 204111 Sec 001

ms = int(input("Input number of milliseconds: "))                #รับค่าเสี้ยววินาที
dy = ms/86400000                                                 #แปลงเสี้ยววินาทีเป็นวัน
hr = (ms%86400000)/3600000                                       #นำเศษจากการคำนวณวันมาแปลงเป็นชั่วโมง
mn = ((ms%86400000)%3600000)/60000                               #นำเศษจากการคำนวณชั่วโมงมาแปลงเป็นนาที
sc = (((ms%86400000)%3600000)%60000)/1000                        #นำเศษจากการคำนวณนาทีมาแปลงเป็นวินาที                
msc = ms%1000                                                    #นำเสี้ยววินาทีจากUserมาแปลงโดยการmod
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)"%(dy,hr,mn,sc,msc))
