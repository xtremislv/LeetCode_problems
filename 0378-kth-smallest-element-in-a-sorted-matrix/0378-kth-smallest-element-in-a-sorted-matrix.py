class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        new = []
        for i in range(m):
            for j in range(n):
                new.append(matrix[i][j])
        new.sort()
        return new[k-1]