from binary_search import binary_search

def sum_giving(a, x):
    for i, n in enumerate(a):
        j = binary_search(a, x - n)
        if j != -1:
            return (i, j)
    return None