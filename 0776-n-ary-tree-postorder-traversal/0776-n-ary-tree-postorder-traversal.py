class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            res.append(node.val)
            
        res = []
        dfs(root)
        return res