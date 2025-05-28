class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobWithCapability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # skip adjacent house
                else:
                    i += 1
            return count >= k

        left, right = min(nums), max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canRobWithCapability(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result