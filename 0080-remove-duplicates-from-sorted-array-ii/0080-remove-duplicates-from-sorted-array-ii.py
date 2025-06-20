from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fd = Counter(nums)
        for key, value in fd.items():
            if value >2:
                fd[key] = 2

        while len(nums) >0:
            nums.pop()
        for key, value in fd.items():
            nums.extend([key]*value)
        return len(nums)
        