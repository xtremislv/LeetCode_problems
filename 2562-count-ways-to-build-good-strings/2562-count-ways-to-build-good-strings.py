class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: 1 way to build an empty string

        for length in range(1, high + 1):
            if length - zero >= 0:
                dp[length] += dp[length - zero]
            if length - one >= 0:
                dp[length] += dp[length - one]
            dp[length] %= MOD

        return sum(dp[low:high + 1]) % MOD