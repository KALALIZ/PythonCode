#!/usr/bin/env python3
#ศิลาลักษณ์ แก้วจันทร์เพชร

def multiplication_table(n):
    print("*", end="\t")
    for x in range(1, n+1):
        print(x, end="\t")
    print('\n')
    for i in range(1,n+1):
        print(i,end='\t')
        for j in range(1,n+1):
            if i > j:
                print(" ", end="\t")
            else:
                print((i)*(j), end="\t")
        print("\n")
        

def main():
    multiplication_table(7)
   

if __name__ == '__main__':
    main()