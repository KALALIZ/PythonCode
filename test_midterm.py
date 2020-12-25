def insertion_sort(list_a):
    size = len(list_a)
    a = list_a[:]

    for i in range(1, size):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        return a

def main(): 
    list_a = [3, 7, 4, 9, 5, 2, 6, 1]
    print(insertion_sort(list_a))


if __name__ == '__main__':
    main()

   