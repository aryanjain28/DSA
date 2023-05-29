import heapq as hq

mList1 = list(set([4, 52, 61, 34, 64, 756, 3, 4, 2, 13, 14, 423, 56, 75, 575]))
mList2 = list(set([31, 62, 13, 52, 635, 6, 56, 74, 7,
              8, 7, 869, 89, 2, 3, 42, 34, 5, 45, 3]))

# hq.heapify(mList1)
# print(mList1)

# hq.heapify(mList2)
# print(mList2)

# mList1 = list(set([4, 52, 61, 34, 64, 756, 3, 4, 2, 13, 14, 423, 56, 75, 575]))
# mList2 = list(set([31, 62, 13, 52, 635, 6, 56, 74, 7,
#               8, 7, 869, 89, 2, 3, 42, 34, 5, 45, 3]))


# mList = list(hq.merge(mList1, mList2))

# print("merged: ", mList)

# hq.heapify(mList)

# print("heap: ", mList)

print(hq.nlargest(2, mList1))
