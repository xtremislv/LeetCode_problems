class Solution(object):
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if not node:
                return -1
            if node.val > root.val:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)

        return dfs(root)