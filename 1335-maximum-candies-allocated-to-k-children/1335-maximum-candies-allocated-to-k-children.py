class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(x):
            # Check if we can distribute at least k piles of size x
            count = 0
            for pile in candies:
                count += pile // x
                if count >= k:
                    return True
            return False

        left, right = 1, max(candies)
        result = 0
    
        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                result = mid  # mid candies per child is possible
                left = mid + 1
            else:
                right = mid - 1

        return result 