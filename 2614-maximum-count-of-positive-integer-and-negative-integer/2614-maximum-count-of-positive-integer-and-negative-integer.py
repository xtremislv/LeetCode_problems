class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count = sum(1 for x in nums if x > 0)
        neg_count = sum(1 for x in nums if x < 0)
        return max(pos_count, neg_count)