from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
    
        # Build prefix sum array where prefix[i] is the number of vowel-strings in words[:i]
        prefix = [0] * (n + 1)

        for i in range(n):
            is_vowel_string = words[i][0] in vowels and words[i][-1] in vowels
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string else 0)

        # Answer each query using prefix sums
        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans