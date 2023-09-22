#
# @lc app=leetcode id=721 lang=python
#
# [721] Accounts Merge
#

# @lc code=start

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, n):
        if n == self.parent[n]:
            return n
        return self.find(self.parent[n])


    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return 
        self.parent[pv] = pu


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        uf = UnionFind(len(accounts))

        mMap = {}        
        for parent, account in enumerate(accounts):
            for email in account[1:]:
                if email not in mMap:
                    mMap[email] = parent
                else:
                    uf.union(mMap[email], parent)

        res = {}
        for email, parent in mMap.items():
            p = uf.find(parent)

            if p not in res:
                res[p] = [accounts[p][0]]

            res[p].append(email)


        return [[r[0]] + sorted(r[1:]) for r in res.values()]
            
 







# @lc code=end

Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])