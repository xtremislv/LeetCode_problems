class Solution(object):
    def minMoves(self, nums):
        from functools import reduce
        return reduce(lambda a, b: a + b, nums) - len(nums) * min(nums)