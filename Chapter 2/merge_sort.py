def merge_sort(a: list) -> list:
    def merge_ranges(start, mid, end):
        a1 = a[start:mid]
        a2 = a[mid:end]

        i = j = 0
        k = start

        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                a[k] = a1[i]
                i += 1
            else:    
                a[k] = a2[j]
                j += 1
            
            k += 1

        if i < len(a1):
            a[k:end] = a1[i:]
        elif j < len(a2):
            a[k:end] = a2[j:]

    def merge_sort_range(start, end):
        if start < end - 1:
            mid = (end + start) // 2
            merge_sort_range(start, mid)
            merge_sort_range(mid, end)
            merge_ranges(start, mid, end)

    merge_sort_range(0, len(a))
    return a

def inplace_merge_sort(a: list) -> list:
    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def merge_ranges(start1, end1, start2, end2, area):
        i = start1
        j = start2

        while i < end1 and j < end2:
            if a[i] < a[j]:
                swap(area, i)
                i += 1
            else:    
                swap(area, j)
                j += 1
            
            area += 1

        while i < end1:
            swap(area, i)
            i += 1
            area += 1

        while j < end2:
            swap(area, j)
            j += 1
            area += 1
    pass