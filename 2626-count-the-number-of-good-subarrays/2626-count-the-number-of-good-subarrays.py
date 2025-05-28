from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        pair_count = 0
        result = 0

        for right in range(len(nums)):
            num = nums[right]
            # Count how many new pairs we add by adding nums[right]
            pair_count += count[num]
            count[num] += 1

            # Shrink window from the left until we no longer have >= k pairs
            while pair_count >= k:
                result += len(nums) - right
                count[nums[left]] -= 1
                pair_count -= count[nums[left]]
                left += 1

        return result