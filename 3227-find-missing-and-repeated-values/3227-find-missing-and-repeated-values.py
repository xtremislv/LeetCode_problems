class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_nums = n * n
        seen = set()
        repeated = -1

        # Flatten the grid and find the repeated number
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                else:
                    seen.add(num)

        # Find the missing number by checking from 1 to n^2
        missing = -1
        for num in range(1, total_nums + 1):
            if num not in seen:
                missing = num
                break

        return [repeated, missing]