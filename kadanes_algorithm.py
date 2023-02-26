
def largest_sum(nums):

    pointer = 0

    start_max = pointer
    end_max = 0

    max_val = nums[0]
    curr = nums[0]

    for i, n in enumerate(nums[1:]):
        i += 1
        if curr > 0:
            curr += n 
        else:
            curr = n
            pointer = i

        if curr > max_val:
            max_val = curr
            start_max = pointer
            end_max = i

    return max_val, nums[start_max:end_max + 1]


max_val, sub = largest_sum([4, -1, 2, -7, 3, 4])
print(max_val, sub)
