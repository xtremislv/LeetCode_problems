class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1: Compute LCS
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)

        lcs = dp[m][n]

        # Step 2: Build the result using LCS
        res = []
        i = j = 0
        for c in lcs:
            # Add characters from str1 until we reach c
            while i < len(str1) and str1[i] != c:
                res.append(str1[i])
                i += 1
            # Add characters from str2 until we reach c
            while j < len(str2) and str2[j] != c:
                res.append(str2[j])
                j += 1
            # Add the LCS character
            res.append(c)
            i += 1
            j += 1

        # Add remaining parts
        res.append(str1[i:])
        res.append(str2[j:])
    
        return ''.join(res)