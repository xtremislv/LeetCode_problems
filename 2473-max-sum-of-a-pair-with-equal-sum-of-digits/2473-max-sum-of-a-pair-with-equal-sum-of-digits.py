from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
    
        max_by_digit_sum = defaultdict(int)
        max_sum = -1

        for num in nums:
            dsum = digit_sum(num)
            if dsum in max_by_digit_sum:
                max_sum = max(max_sum, num + max_by_digit_sum[dsum])
                max_by_digit_sum[dsum] = max(max_by_digit_sum[dsum], num)
            else:
                max_by_digit_sum[dsum] = num

        return max_sum