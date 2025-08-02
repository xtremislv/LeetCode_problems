from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
        def backtrack(r =0, c =0):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r+1, 0)
            if board[r][c] != '.':
                return backtrack(r, c+1)
            box_index = (r // 3) * 3 + (c//3)
            for digit in map(str, range(1,10)):
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_index]:
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_index].add(digit)
                    if backtrack(r, c+1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_index].remove(digit)
            return False
        backtrack()
        