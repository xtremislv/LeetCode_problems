class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        from functools import reduce
        a, b, f =reduce(
            lambda r, x: (
                (x, r[1], r[2]) if x <= r[0] else
                (r[0], x if x <= r[1] else r[1], True if x > r[1] else r[2])
            
            ), nums, (float('inf'), float('inf'), False)
        )
        return f