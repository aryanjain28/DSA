def quick_sort(list):
    sorted_list = []

    if len(list) <= 1:
        return list
    
    left_half = []
    right_half = []
    pivot = list[0]

    for value in list[1:]:
        if value < pivot:
            left_half.append(value)
        else:
            right_half.append(value)

    left = quick_sort(left_half)
    right = quick_sort(right_half)

    sorted_list = left + [pivot] + right
    return sorted_list

print(quick_sort([5,8,1,7,2]))