from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        central = False

        for word in list(count.keys()):  # fix: iterate over list of keys
            rev = word[::-1]
            if word != rev:
                pair_count = min(count[word], count[rev])
                length += pair_count * 4
                count[word] -= pair_count
                count[rev] -= pair_count
            else:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] %= 2
                if count[word] == 1:
                    central = True

        if central:
            length += 2

        return length