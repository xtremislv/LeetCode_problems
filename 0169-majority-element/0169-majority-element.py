from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq = Counter(nums)
        for key, value in frq.items():
            if value == max(frq.values()):
                return key