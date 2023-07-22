#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

import heapq
# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """


        mStack = []
        for i in range(len(position)):
            mStack.append((position[i], speed[i]))

        mStack.sort()

        fleets = len(position)
        while len(mStack) > 1:
            c1Pos, c1speed = mStack.pop()
            c2Pos, c2speed = mStack.pop()

            if ((target - c1Pos) / c1speed) >= ((target - c2Pos) / c2speed):
                mStack.append((c1Pos, c1speed))
                fleets -= 1
            else:
                mStack.append((c2Pos, c2speed))

        return fleets



        # heap = []
        # for i in range(len(position)):
        #     heapq.heappush(heap, (-position[i], speed[i]))

        # fleets = len(position)
        # while len(heap) > 1:

        #     c1Pos, c1speed = heapq.heappop(heap)
        #     c2Pos, c2speed = heapq.heappop(heap)
            
        #     if ((target + c1Pos) / c1speed) >= ((target + c2Pos) / c2speed):
        #         heapq.heappush(heap, (c1Pos, c1speed))
        #         fleets -= 1
        #     else:
        #         heapq.heappush(heap, (c2Pos, c2speed))


        # return fleets



        
# @lc code=end
Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
# Solution().carFleet(100, [0,2,4], [4,2,1])
# Solution().carFleet(10, [6,8], [3,2])
