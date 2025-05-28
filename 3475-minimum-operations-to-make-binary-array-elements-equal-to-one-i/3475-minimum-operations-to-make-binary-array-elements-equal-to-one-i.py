class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n - 2):
            if nums[i] == 0:
                # Flip nums[i], nums[i+1], nums[i+2]
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1

        # Check if the remaining elements are all 1s
        if nums[-2:] != [1, 1] and n >= 2:
            return -1
        if n == 1 and nums[0] != 1:
            return -1
        return operations