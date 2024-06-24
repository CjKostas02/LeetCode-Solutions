# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)

# dp, combinatorics, sliding window, two pointers
class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [1]
        prev = 0
        for i in xrange(n):
            if lookup[i] != -1:  # optimized
                dp = [reduce(lambda total, i: (total+dp[i])%MOD, xrange(max((lookup[i]-i)-prev, 0), min((lookup[i]+1)-prev, len(dp))), 0)]
                prev = lookup[i]
                continue
            new_dp = [0]*min(len(dp)+((i+1)-1), (lookup[-1]+1)-prev)
            for j in xrange(len(new_dp)):
                new_dp[j] = dp[j] if j < len(dp) else 0
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]


# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)
# dp, combinatorics, sliding window, two pointers
class Solution2(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [0]*(lookup[-1]+1)
        dp[0] = 1
        for i in xrange(n):
            new_dp = [0]*len(dp)
            if lookup[i] != -1:  # optimized
                new_dp[lookup[i]] = reduce(lambda total, i: (total+dp[i])%MOD, xrange(max(lookup[i]-i, 0), lookup[i]+1), 0)
            else:
                for j in xrange(len(dp)):
                    new_dp[j] = dp[j]
                    if j-1 >= 0:
                        new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                    if j-(i+1) >= 0:
                        new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]


# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)
# dp, combinatorics, sliding window, two pointers
class Solution3(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [0]*(lookup[-1]+1)
        dp[0] = 1
        for i in xrange(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in xrange(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr if lookup[i] == -1 or lookup[i] == j else 0
            dp = new_dp
        return dp[-1]
