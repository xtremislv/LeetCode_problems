class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        from functools import reduce
        a %= 1337
        return reduce(lambda r, d: pow(r, 10, 1337) * pow(a, d, 1337) % 1337, b, 1)