from typing import List
from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(w1, w2):
            if len(w1) != len(w2):
                return -1
            return sum(a != b for a, b in zip(w1, w2))

        n = len(words)
        # DP: dp[i] = (length of best path ending at i, parent_index)
        dp = [(1, -1) for _ in range(n)]

        # Check all pairs i < j for valid transitions
        for i in range(n):
            for j in range(i + 1, n):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_distance(words[i], words[j]) == 1:
                    # Try extending i -> j
                    if dp[i][0] + 1 > dp[j][0]:
                        dp[j] = (dp[i][0] + 1, i)

        # Find the end of the longest path
        max_len, end = max((length, idx) for idx, (length, _) in enumerate(dp))

        # Reconstruct path
        path = []
        while end != -1:
            path.append(end)
            end = dp[end][1]
        path.reverse()

        return [words[i] for i in path]
