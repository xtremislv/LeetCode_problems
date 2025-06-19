class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1  # At least one subsequence is needed
        start = nums[0]

        for num in nums:
            if num - start > k:
                count += 1
                start = num  # Start a new subsequence

        return count