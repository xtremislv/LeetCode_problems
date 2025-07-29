class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        v20, v01, v10, v11 = 0, -100005, 0, -100005
        for x in prices:
            v01 = max(-x, v01)
            v10 = max(v01 + x, v10)
            v11 = max(v10 - x, v11)
            v20 = max(v11 + x, v20)
        return max([v01, v10, v11, v20])