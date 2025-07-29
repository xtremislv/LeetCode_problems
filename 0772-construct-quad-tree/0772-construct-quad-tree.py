"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x,y,size):
            if size == 1:
                return Node(grid[x][y] == 1, True)
            half = size //2
            top_left = build(x,y,half)
            top_right =build(x, y + half, half)
            bottom_left = build(x +half, y, half)
            bottom_right = build(x +half, y+half, half)
            if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)

        return build(0,0,len(grid))