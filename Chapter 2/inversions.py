def count_inversions(arr):
    def merge_counting(start, mid, end):
        s = arr[start:mid]
        e = arr[mid:end]

        inversions = 0
        added_from_end = 0

        k = start
        i = 0
        j = 0
        while i < len(s) and j < len(e):
            if s[i] <= e[j]:
                arr[k] = s[i]
                inversions += added_from_end
                i += 1
            else:
                arr[k] = e[j]
                added_from_end += 1
                j += 1
            k += 1

        if i < len(s):
            arr[k:end] = s[i:]
        elif j < len(e):
            arr[k:end] = e[j:]

        inversions += (len(s) - i) * added_from_end
        return inversions

    def count_inversions_in_range(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            x = count_inversions_in_range(start, mid)
            y = count_inversions_in_range(mid, end)
            return x + y + merge_counting(start, mid, end)
        else:
            return 0

    return count_inversions_in_range(0, len(arr))