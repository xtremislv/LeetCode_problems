import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairAllCars(time_limit):
            total = 0
            for r in ranks:
                # max cars this mechanic can repair in time_limit
                max_cars = int(math.isqrt(time_limit // r))
                total += max_cars
            return total >= cars

        # Binary search on time from 1 to max possible time
        left, right = 1, min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            if canRepairAllCars(mid):
                right = mid
            else:
                left = mid + 1

        return left