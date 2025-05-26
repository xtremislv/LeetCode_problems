from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        freq = [0] * (n + 1)

        # Difference array to accumulate range frequency
        for l, r in queries:
            freq[l] += 1
            if r + 1 < len(freq):
                freq[r + 1] -= 1

        # Prefix sum to get actual frequency per index
        for i in range(1, n):
            freq[i] += freq[i - 1]

        # Check if each index can be decremented enough times
        for i in range(n):
            if nums[i] > freq[i]:
                return False

        return True
