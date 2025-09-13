from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @lru_cache(None)
        def dfs(i, p):
            if i == len(key):
                return 0
            res = float('inf')
            for j in pos[key[i]]:
                dist = abs(p - j)
                step = min(dist, n - dist) + 1
                res = min(res, step + dfs(i + 1, j))
            return res
    
        n = len(ring)
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        return dfs(0, 0)