class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for x in range(1,len(nums)):
            if nums[x] != nums[i-1]:
                nums[i] = nums[x]
                i+= 1

        return i
