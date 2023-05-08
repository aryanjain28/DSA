
def merge(left, right):

    i = 0
    j = 0
    res = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort([1,5,2,1,1221,6,7,8,-14,1,1,4,24,2,56,0,65,645,6456,4]))
