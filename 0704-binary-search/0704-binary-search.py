"""
Time: O(NLogN) where N = len(nums)
Binary search loop
Space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Mid is too small, move left forward
                left = mid + 1
            else:
                # Mid is too big, move right backwards
                right = mid - 1
        
        return -1