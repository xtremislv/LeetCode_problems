# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        self._recover(root, 0)
    
    def _recover(self, node, val):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self._recover(node.left, 2 * val + 1)
        self._recover(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)