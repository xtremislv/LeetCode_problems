class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        numbers = list(range(1, n+1))
        fact = factorial(n)
        k -= 1
        result = []
        for i in range(n):
            fact //= (n - i)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact
        return ''.join(result)