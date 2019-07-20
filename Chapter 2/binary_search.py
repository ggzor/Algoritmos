def binary_search(a, elem):
    l = 0
    r = len(a)
    while l < r:
        m = (r + l) // 2
        if a[m] == elem:
            return m
        elif elem < a[m]:
            r = m
        else:
            l = m + 1

    return -1