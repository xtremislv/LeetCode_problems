import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = []
        for num in reversed(nums):
            insert_pos = bisect.bisect_left(sorted_nums, num)
            result.append(insert_pos)
            bisect.insort(sorted_nums, num)
        return result[::-1]