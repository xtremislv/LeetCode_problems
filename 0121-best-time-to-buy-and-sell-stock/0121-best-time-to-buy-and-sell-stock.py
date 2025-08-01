class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        j = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < j:
                j = prices[i]
            elif prices[i] - j > profit:
                profit = prices[i] - j
        return profit