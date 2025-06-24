from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
    
        # First, collect all indices where nums[i] == key
        key_indices = [i for i, val in enumerate(nums) if val == key]
    
        # For each key index, add all indices within distance k
        for i in key_indices:
            for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                result.add(j)
    
        return sorted(result)