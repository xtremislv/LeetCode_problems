class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]
                k = index.get(x, -1)
                if k >= 0 and k < i:
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])

        return max_len if max_len >= 3 else 0