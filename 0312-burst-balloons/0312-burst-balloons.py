class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for l in range(2,n):
            for i in range(n-l):
                j = i+l
                m = 0
                ai, aj = nums[i], nums[j]
                for k in range(i+1, j):
                    m = max(m, dp[i][k] + dp[k][j] + ai*nums[k]*aj)
                dp[i][j] = m
        return dp[0][-1]