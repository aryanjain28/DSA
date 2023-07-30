#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

from heapq import heappop, heappush
# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        heap = []
        for task, count in counter.items():
            heappush(heap, (-count, -1, task))

        q = []
        curr = 0
        while heap or q:
            
            if q:
                count, i, task = q[0]
                if curr - i > n or i == -1:
                    heappush(heap, q.pop(0))

            if heap:
                count, i, task = heap[0]
                if curr - i > n or i == -1:
                    heappop(heap)
                    if count + 1 != 0:
                        q.append((count+1, curr, task))

            curr += 1

        return curr



        
# @lc code=end
print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
# print(Solution().leastInterval(["A","A","A","B","B","B"], 0))
# print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
