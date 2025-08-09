class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import reduce
        a, b, c = reduce(
            lambda x, p: (max(x[0], x[2] - p), x[0] + p, max(x[2], x[1])), prices, (float('-inf'), 0, 0)
        )
        return max(b, c)