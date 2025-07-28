class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o ="O"
        n = len(board)
        m = len(board[0])
        q = deque()
        for i in range(n):
            if board[i][0] == o:
                q.append((i,0))
            if board[i][m-1] == o:
                q.append((i, m-1))
            
        for j in range(m):
            if board[0][j] == o:
                q.append((0,j))
            if board[n-1][j] == o:
                q.append((n-1, j))

        def inBound(i, j):
            return (0 <= i < n) and (0 <= j < m)
        
        while q:
            i, j = q.popleft()
            board[i][j] = "#"

            for ii , jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not inBound(ii, jj):
                    continue
                if board[ii][jj] != o:
                    continue
                q.append((ii, jj))
                board[ii][jj] = '#'

        for i in range(n):
            for j in range(m):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = o
        