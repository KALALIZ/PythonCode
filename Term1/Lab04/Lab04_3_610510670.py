 

 #!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Ploblem 3
# 204111 Sec 001


def calculate_p2p_evolve_exp(p, c):
    #if p > c :
    ans1 = abs((c + (p-1))//12)*500
    #else:
    ans2 = p*500
    if ans1 > ans2:
        return ans2
    else:
        return ans1
        
def main():
    #รับค่า Pidgey
    p = int(input("Input Pidgey: "))

    #รับค่า Candy
    c = int(input("Input Candy: "))

    #คำนวณค่า EXP และ Candy ที่ได้จากการแปลงร่างเป็น Pidgeotto
    ans = calculate_p2p_evolve_exp(p, c)

    #แสดงผลค่าที่คำนวณได้
    print(ans)



    
    
    
if __name__ == "__main__":
    main()

   
