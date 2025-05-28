class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Shift zeros to the end
        res = [num for num in nums if num != 0]
        zeros_count = n - len(res)
        res.extend([0] * zeros_count)
        return res
