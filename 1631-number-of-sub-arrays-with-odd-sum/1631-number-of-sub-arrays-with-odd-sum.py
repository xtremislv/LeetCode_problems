class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1  # prefix sum 0 is even
        result = 0
        prefix = 0

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

        return result % MOD