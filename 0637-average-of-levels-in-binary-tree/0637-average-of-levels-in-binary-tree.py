# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue =deque([root])
        while queue:
            levelSize = len(queue)
            levelTotal = 0

            for _ in range(levelSize):
                node = queue.popleft()
                levelTotal += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(levelTotal/levelSize)
        return res