class Solution(object):
    def findDuplicates(self, nums):
        r = [abs(x) for x in nums if nums[abs(x) - 1] < 0 or (nums.__setitem__(abs(x) - 1, -nums[abs(x) - 1]) is None and 0)]
        return r