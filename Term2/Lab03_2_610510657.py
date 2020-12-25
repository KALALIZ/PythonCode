#!/usr/bin/env python3
# ปรียารัตน์ จับจ่าย
# 610510657
# Lab 03
# Problem 2
# 204113 Sec 002

def main():
    print(IP_encode(2,'3232237069'))
    print(IP_encode(1,'10.28.4.2'))
    print(IP_encode(2,'169608194'))
    print(IP_encode(1,'192.168.6.13'))

def IP_encode(int_m,str_t):
    if int_m == 1:
        t = str_t.split('.')
        t1 = format(int(t[0]),'08b')
        t2 = format(int(t[1]),'08b')
        t3 = format(int(t[2]),'08b')
        t4 = format(int(t[3]),'08b')
        t_a  = str(t1) + str(t2) + str(t3) + str(t4)
        x = int(str(t_a), 2)
        return x
    elif int_m == 2:
        a = format(int(str_t),'032b')
        #print(a)
        #return
        t1_1 = ''
        t2_2 = ''
        t3_3 = ''
        t4_4 = ''
        for i in range(8):
            t1_1 += a[i] 
            t2_2 += a[i+8]
            t3_3 += a[i+16]
            t4_4 += a[i+24]
        t_all = str(int((t1_1),2)) + '.' + str(int((t2_2),2)) + '.' + str(int((t3_3),2)) + '.' + str(int((t4_4),2))
        return t_all



if __name__ == '__main__':
    main()
    
