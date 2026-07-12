class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1

            for j in range(i, n):
                product *= nums[j]

                if product < k:
                    ans += 1
                else:
                    break

        return ans