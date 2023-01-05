def sum(list):
    if not list: return 0
    remaining_sum = sum(list[1:])
    return list[0] + remaining_sum

print(sum([1,2,3,4,5]))
    
    