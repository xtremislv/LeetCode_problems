from collections import Counter
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            next_count = [0] * 26
            for i in range(25):  # 'a' to 'y'
                next_count[i + 1] = (next_count[i + 1] + count[i]) % MOD
            # Handle 'z' -> 'a' + 'b'
            next_count[0] = (next_count[0] + count[25]) % MOD
            next_count[1] = (next_count[1] + count[25]) % MOD
            count = next_count

        return sum(count) % MOD
