import random

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i+1]:
            return False
    return True

def bogo_sort(values):
    i = 0
    while not is_sorted(values):
        i += 1
        random.shuffle(values)
    print("i: ", i)
    return values

print(bogo_sort([4,1,8,3,2]))        



