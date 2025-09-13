class Solution:
    def updateMatrix(self, mat):
        n, m = len(mat), len(mat[0])
        dist = [[-1] * m for _ in range(n)]
        q = deque()

        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]

        # 1. Enqueue all cells with 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0

        # Multi-source BFS
        while q:
            row, col = q.popleft()
            for k in range(4):
                newRow = row + dRow[k]
                newCol = col + dCol[k]

                if 0 <= newRow < n and 0 <= newCol < m and dist[newRow][newCol] == -1:
                    dist[newRow][newCol] = dist[row][col] + 1
                    q.append((newRow, newCol))

        return dist