from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack(counter):
            total = 0
            for char in counter:
                if counter[char] == 0:
                    continue
                # Choose the character
                counter[char] -= 1
                total += 1  # count this sequence
                total += backtrack(counter)
                counter[char] += 1  # backtrack
            return total

        return backtrack(count)