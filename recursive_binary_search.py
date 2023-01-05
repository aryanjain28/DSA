def recursive_binary_saarch(list, target):
    
    print(list)

    if(len(list) == 0):
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                recursive_binary_saarch(list[midpoint+1:], target)
            elif list[midpoint] > target:
                recursive_binary_saarch(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

arr = [1,2,3,4,5,6,7,8]
target = 52

res = recursive_binary_saarch(arr, target)
verify(res)

