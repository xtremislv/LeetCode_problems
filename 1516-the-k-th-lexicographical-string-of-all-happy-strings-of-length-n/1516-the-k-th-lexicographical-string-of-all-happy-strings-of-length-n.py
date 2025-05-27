class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []

        def dfs(path):
            if len(result) == k:
                return
            if len(path) == n:
                result.append(path)
                return
            for ch in 'abc':
                if not path or path[-1] != ch:
                    dfs(path + ch)

        dfs('')
        return result[-1] if len(result) == k else ''