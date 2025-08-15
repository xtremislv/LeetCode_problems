# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.maxVal = float('-inf')
    def helper(self, node):
        if not node:
            return
        oldMax = self.maxVal
        self.maxVal = max(self.maxVal, node.val)
        if node.val == self.maxVal:
            self.count += 1
        self.helper(node.left)
        self.helper(node.right)
        self.maxVal = oldMax
    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root)
        return self.count