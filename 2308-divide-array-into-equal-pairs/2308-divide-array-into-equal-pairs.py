from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for freq in count.values():
            if freq % 2 != 0:
                return False
        return True