class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        result = 10
        current = 9
        for i in range(2,n+1):
            current *= (10 - (i-1))
            result += current
        return result