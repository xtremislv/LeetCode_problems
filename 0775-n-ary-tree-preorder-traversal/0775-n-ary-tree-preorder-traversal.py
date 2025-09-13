class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        def dfs(u):
            if not u:
                return
            res.append(u.val)
            for v in u.children:
                dfs(v)
        res = []
        dfs(root)
        return res