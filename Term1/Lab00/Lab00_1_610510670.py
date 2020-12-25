#!/usr/bin/env python3
#ศิลาลักษณ์ แก้วจันทร์เพชร

def main():
    print("Input student grades with this format: ", end="")
    print("\'Student ID;Grade1, Grade2, ..., GradeN\': ")
    grades_str = input()
    student_id, gpa_major = compute_major_gpa(grades_str)
    print("Student ID = %s, Major G.P.A. = %.2f" %(student_id, gpa_major))

def compute_major_gpa(grades_str):
    x = grades_str
    y = x.split(';')
    id = y[0]
    z = (y[1]).split(',')
    result = 0
    for i in z:
        if i == 'A':
            result += 4
        elif i == 'B+':
            result += 3.5
        elif i == 'B':
            result += 3
        elif i == 'C+':
            result += 2.5
        elif i == 'C':
            result += 2
        elif i == 'D+':
            result += 1.5
        elif i == 'D':
            result += 1
        elif i == 'F':
            result += 0
    gpa = (result*3) / ((len(z) * 3))
    return (id, gpa)





if __name__ == '__main__':
    main()