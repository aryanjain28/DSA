def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return -1

def verify(r):
    if r != -1:
        print("Target found at: ", r)
    else:
        print("Not Found")

arr = [1,2,3,4,5,6,7,8]
target = 2

r = linear_search(arr, target)
verify(r)