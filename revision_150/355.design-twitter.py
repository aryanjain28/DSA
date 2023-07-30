#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

from heapq import heappush, heappop
# @lc code=start
class Twitter(object):

    def __init__(self):
        self.users = {}
        self.posts = []
        self.count = 0
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        heappush(self.posts, (self.count, userId, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        temp = [p for p in self.posts]
        while len(res) < 10 and temp:
            _, poster, tId = heappop(temp)
            if poster == userId or (userId in self.users and poster in self.users[userId]):
                res.append(tId)

        return res
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users:
            self.users[followerId] = set()
        
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.users and followeeId in self.users[followerId]: 
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

