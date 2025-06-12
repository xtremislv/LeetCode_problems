class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        first = abs(nums[0] - nums[-1])
        diffs = []
        diffs.append(first)
        for s in range(len(nums)-1):
            df = abs(nums[s] - nums[s+1])
            diffs.append(df)
        return max(diffs)