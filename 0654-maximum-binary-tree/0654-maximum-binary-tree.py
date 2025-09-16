# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            # monotonic stack for assigning left and right childs accordingly.
            node = TreeNode(num)
            # assign left child to the current node if it has higher value
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            # assign right child to the top element of the stack
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]