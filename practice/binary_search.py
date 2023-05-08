

def binary_search(arr, target):

    i = 0
    j = len(arr) - 1

    while i <= j:

        mid = (i + j) // 2

        if arr[mid] < target:
            i = mid + 1
        elif arr[mid] > target:
            j = mid - 1
        else:
            return mid

    return -1

print(binary_search([1,6,7,11,42,55], 55))
