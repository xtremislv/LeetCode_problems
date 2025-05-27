from typing import List
from collections import Counter
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])

        # Step 1: Count frequency of each character at each position
        freq = [Counter() for _ in range(n)]
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ch] += 1

        # Step 2: DP table dp[i][j] = number of ways to form target[i:] using word columns j:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        # Base case: there's 1 way to form an empty target
        for j in range(n + 1):
            dp[m][j] = 1

        # Fill DP table from bottom up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Option 1: skip current column
                dp[i][j] = dp[i][j + 1] % MOD
                # Option 2: use current column if character matches
                ch = target[i]
                if ch in freq[j]:
                    dp[i][j] += freq[j][ch] * dp[i + 1][j + 1]
                    dp[i][j] %= MOD

        return dp[0][0]
        