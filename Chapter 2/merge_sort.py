def merge_sort(a: list) -> list:
    def merge_ranges(start1, start2, end):
        for i in range(start1, end + 1):
            pass

    def merge_sort_range(start, end):
        if start < end:
            mid = (end - start) // 2
            merge_sort_range(start, mid)
            merge_sort_range(mid + 1, end)
            merge_range(start, mid, end)

    merge_sort_range(0, len(a) - 1)
    return a

"""
b = [1, 2, 16, 18, 20, 15, 3, 6, 10, 17]
len(a) = 10


"""