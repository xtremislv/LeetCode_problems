class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tg = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        count = 0
        for s in grid:
            for t in tg:
                if t == s:
                    count += 1
        return count
        