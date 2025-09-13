class Solution:
    def __init__(self):
        self.sum = 0  # cumulative sum

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return
            
            # 1. Go right first
            traverse(node.right)

            # 2. Process current node
            self.sum += node.val
            node.val = self.sum

            # 3. Go left
            traverse(node.left)

        traverse(root)
        return root