#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        mMap = {}
        for index in range(len(position)):
            mMap[position[index]] = speed[index]

        stack = []
        for curr_pos in range(target-1, -1, -1):
            if curr_pos in mMap:
                curr_time = (target - curr_pos) / mMap[curr_pos]
                if not stack:
                    stack.append(curr_time)
                    continue

                last_time = stack[-1]
                if last_time < curr_time:
                    stack.append(curr_time)

        return len(stack)


        
# @lc code=end
# print(Solution().carFleet(12, [10,8,0,5,3], speed = [2,4,1,1,3]))
# print(Solution().carFleet(10, [3], speed = [3]))
# print(Solution().carFleet(100, [0,2,4], speed = [4,2,1]))
print(Solution().carFleet(10, [6,3], speed = [3,2]))
