#
# @lc app=leetcode id=2149 lang=python
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(left, right):

            res = [0] * (len(left) + len(right))
            i, j = 0, 0
            index = 0

            index = 0
            for n in left:
                if n < 0:
                    pass
                else:
                    pass

                index += 1

            # while len(res) < len(left) + len(right):
            #     # even: POSITVE
            #     if index % 2 == 0:
            #         pass
            #     # odd: NEGATIVE
            #     else:
            #         pass

            #     res.append(left[index])
            #     index += 1

            return left + right

            


        def split(arr):

            if len(arr) <= 1:
                return arr
        
            left = split(arr[:len(arr) // 2])
            right = split(arr[len(arr) // 2:])

            print(left, right)

            return merge(left, right)
        
        split(nums)




        
# @lc code=end

Solution().rearrangeArray([3,1,-2,-5,2,-4])