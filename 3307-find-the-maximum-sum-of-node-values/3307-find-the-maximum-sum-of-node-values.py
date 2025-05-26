from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base_sum = sum(nums)
        dp = [0, float('-inf')]  # dp[0] = even count XORed, dp[1] = odd count XORed

        for num in nums:
            diff = (num ^ k) - num
            new_dp = dp[:]
            new_dp[0] = max(dp[0], dp[1] + diff)
            new_dp[1] = max(dp[1], dp[0] + diff)
            dp = new_dp

        return base_sum + dp[0]
