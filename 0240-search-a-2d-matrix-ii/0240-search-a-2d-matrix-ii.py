class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # start at top-right

        while row < rows and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True  # found target
            elif target < current:
                col -= 1  # move left
            else:
                row += 1  # move down
        return False  # target not found