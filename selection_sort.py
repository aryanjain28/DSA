

def selection_sort(values):
    sorted_list = []
    min = -1

    print("%-25s %-25s" % (values, sorted_list))
    while len(values) > 0:
        min =  values[0]
        index = 0
        for i in range(0, len(values)):
            if values[i] < min: 
                min = values[i]
                index = i
        sorted_list.append(values.pop(index))
        print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

# print("Final: ", selection_sort([5,2,1,1,7,3]))
    
temp = [5,2,1,1,7,3]


        



