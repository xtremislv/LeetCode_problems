from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        for perm in permutations(digits, 3):
            # Leading zero check
            if perm[0] == 0:
                continue
            # Even number check (last digit must be even)
            if perm[2] % 2 != 0:
                continue
            number = perm[0] * 100 + perm[1] * 10 + perm[2]
            result.add(number)
        return sorted(result)

            

        