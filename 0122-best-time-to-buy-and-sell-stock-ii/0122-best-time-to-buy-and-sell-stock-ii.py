class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -1 * prices[0]

        for x in range(1, len(prices)):
            dp[x][0] = max(dp[x-1][0], dp[x-1][1] + prices[x])
            dp[x][1] = max(dp[x-1][1], dp[x-1][0] - prices[x])

        return dp[-1][0]