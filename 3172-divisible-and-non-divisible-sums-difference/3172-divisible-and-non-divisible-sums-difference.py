class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        count = n // m
        divisible_sum = m * count * (count + 1) // 2
        return total_sum - 2 * divisible_sum
