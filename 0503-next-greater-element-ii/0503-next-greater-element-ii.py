class Solution(object):
    def nextGreaterElements(self, nums):
        return [next((x for x in nums[i+1:] + nums[:i] if x > nums[i]), -1) for i in range(len(nums))]