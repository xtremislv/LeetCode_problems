class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            # Check divisors up to sqrt(num)
            limit = int(num ** 0.5) + 1
            for i in range(3, limit, 2):
                if num % i == 0:
                    return False
            return True

        prev_prime = -1
        min_gap = float('inf')
        result = [-1, -1]

        for num in range(left, right + 1):
            if is_prime(num):
                if prev_prime != -1 and (num - prev_prime) < min_gap:
                    min_gap = num - prev_prime
                    result = [prev_prime, num]
                prev_prime = num

        return result