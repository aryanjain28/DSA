def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:

        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1


    return -1

def verify(r):
    if r != -1:
        print("Target found at: ", r)
    else:
        print("Not Found")

arr = [1,2,3,4,5,6,7,8]
target = 5

r = binary_search(arr, target)
verify(r)