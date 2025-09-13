class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r0, c0 = click

        # 1) If you click on a mine → X and done
        if board[r0][c0] == 'M':
            board[r0][c0] = 'X'
            return board

        # 8 directions around a cell
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def dfs(i: int, j: int):
            # 2) Count adjacent mines in one pass
            mine_count = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                    mine_count += 1

            # 3) If there are mines around, show the count and stop
            if mine_count > 0:
                board[i][j] = str(mine_count)
                return

            # 4) Otherwise, mark as blank ('B') and recurse into neighbors
            board[i][j] = 'B'
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                # only recurse on unrevealed empties 
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'E':
                    dfs(ni, nj)

        # 5) Start the reveal
        dfs(r0, c0)
        return board


# PS. Only recurses on neighbours when you’ve just turned a cell to 'B' so that you don't need a visit array or set