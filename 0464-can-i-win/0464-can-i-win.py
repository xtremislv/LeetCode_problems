class Solution:
    def canIWin(self, max_int: int, total: int) -> bool:
        if max_int * (max_int + 1) / 2 < total:
            return False

        if total <= max_int:
            return True

        dp = {}

        def dfs(mask: int, current: int):
            if mask in dp:
                return dp[mask]

            for i in range(max_int):
                if mask & (1 << i):
                    continue

                if i + 1 + current >= total or not dfs(mask | (1 << i), current + i + 1):
                    dp[mask] = True
                    return True

            dp[mask] = False
            return False

        return dfs(0, 0)