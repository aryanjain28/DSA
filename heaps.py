
# 1. Structure Property
# values are added left to right
# complete bin tree.

# 2. Order Property.
# root is always the minimum (or maximum)
# every value in the left and in the right
#   subtree will be greater than the root.

# We can also have duplicates in heaps.

class Heap:

    def __init__(self) -> None:
        self.heap = [0]

    def push(self, val) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1

        while self.heap[index // 2] > self.heap[index]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def pop(self, val) -> int:
        pass

heap = Heap()
heap.push(14)
heap.push(19)
heap.push(16)
heap.push(21)
heap.push(26)
heap.push(19)
heap.push(68)
heap.push(10)


print(heap.heap)
