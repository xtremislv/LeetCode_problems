# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            res = max(res, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val
        dfs(root)
        return res