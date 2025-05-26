from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zero1 = 0, 0
        for x in nums1:
            if x == 0:
                zero1 += 1
            else:
                sum1 += x

        sum2, zero2 = 0, 0
        for x in nums2:
            if x == 0:
                zero2 += 1
            else:
                sum2 += x

        # Minimum possible sums after replacing zeros with 1
        min_possible_sum1 = sum1 + zero1
        min_possible_sum2 = sum2 + zero2

        # Start from max of the two minimal sums
        target = max(min_possible_sum1, min_possible_sum2)

        # Check if it's possible to reach this target from both sides
        if target - sum1 > zero1 * 10**11:
            return -1
        if target - sum2 > zero2 * 10**11:
            return -1

        return target
