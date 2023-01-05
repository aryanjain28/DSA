def split_list(list):
    midpoint = len(list) // 2
    return list[:midpoint], list[midpoint:]

def merge(left, right):

    l = []
    i = 0
    j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left): 
        l.append(left[i])
        i += 1
    
    while j < len(right): 
        l.append(right[j])
        j += 1
    
    return l

def merge_sort(list):

    if len(list) <= 1: 
        return list

    left_half, right_half = split_list(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    sorted = merge(left, right)

    return sorted

print("Sorted: ", merge_sort([12,52,10,1,45]))