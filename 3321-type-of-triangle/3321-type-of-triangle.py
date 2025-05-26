from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)

        # Step 1: Triangle inequality check
        if a + b <= c:
            return "none"

        # Step 2: Classify triangle
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
