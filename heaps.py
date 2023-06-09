
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
        self.heap = []

    def push(self, val) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        # parent > last_appended_val => swap with parent
        while self.heap[i // 2] > self.heap[i]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        print("Val: ", val)
        print("sleself.heap: ", self.heap)

    def heapify(self):

        index = 1
        LEN = len(self.heap)
        while True:
            # check if it has right child, meaning it has both child?
            if index*2+1 < LEN:
                # check for minimum
                if self.heap[index*2] < self.heap[index*2+1] and self.heap[index*2] < self.heap[index]:
                    self.heap[index*2], self.heap[index] = self.heap[index], self.heap[index*2]
                    index *= 2
                elif self.heap[index*2] > self.heap[index*2+1] and self.heap[index*2+1] < self.heap[index]:
                    self.heap[index*2 +
                              1], self.heap[index] = self.heap[index], self.heap[index*2+1]
                    index = index * 2 + 1
                else:
                    break
            # check if it has left child?
            elif index*2 < LEN and self.heap[index] > self.heap[index*2]:
                self.heap[index*2], self.heap[index] = self.heap[index], self.heap[index*2]
                index *= 2
            else:
                break

    def pop(self) -> int:

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popval = self.heap.pop()
        self.heapify()
        return popval


heap = Heap()
heap.push(21)
heap.push(26)
heap.push(14)
heap.push(19)
heap.push(16)
heap.push(19)
heap.push(68)
heap.push(10)


print(heap.pop())
