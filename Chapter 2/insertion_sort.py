from random import randint

def insertion_sort_pythonic(a):
    for i in range(1, len(a)):
        for j in range(i - 1, -1, -1):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                break

    return a

def insertion_sort_classic(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and key < a[i]:
            a[i + 1] = a[i]
            i -= 1

        a[i + 1] = key

    return a

def reverse_insertion_sort_classic(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and key > a[i]:
            a[i + 1] = a[i]
            i -= 1

        a[i + 1] = key

    return a
