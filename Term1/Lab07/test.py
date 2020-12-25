def main():
    n = int(input(""))
    triangle(n)


def triangle(n):
    for i in range(n):
        for j in range(n):
            if (i <= j) :
                print(j+1, end=" ")
            else:
                print(".", end=" ")
           
        print()


if __name__ == '__main__':
    main()
