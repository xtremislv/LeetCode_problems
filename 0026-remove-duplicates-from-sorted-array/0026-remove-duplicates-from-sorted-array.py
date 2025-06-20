class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq =[]
        for s in nums:
            if s not in unq:
                unq.append(s)
        
        while len(nums) >0:
            nums.pop()
        for a in unq:
            nums.append(a)
        return len(nums)