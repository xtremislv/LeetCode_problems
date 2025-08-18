class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums = list(map(str, nums))
        nums.sort(key = lambda x: x * 10, reverse = True)
        res = "".join(nums)
        return "0" if res[0] == "0" else res