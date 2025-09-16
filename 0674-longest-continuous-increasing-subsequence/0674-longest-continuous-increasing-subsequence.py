class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 1
        curr_len = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr_len +=1
                max_len = max(max_len,curr_len)
            else:
                curr_len = 1
        return max_len
        