class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(x, c =0):
            if x == 1:
                return c
            if x % 2 == 0:
                return helper(x >>1, c + 1)
            else:
                if x == 3 or not ((x >>1) & 1):
                    return helper(x-1, c+1)
                else:
                    return helper(x+1, c+1)
        return helper(n)