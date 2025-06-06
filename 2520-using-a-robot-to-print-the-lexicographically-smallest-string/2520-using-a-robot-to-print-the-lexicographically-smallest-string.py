class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        min_suffix = [None] * len(s)
        min_char = 'z'

        # Precompute the minimum character from position i to the end
        for i in reversed(range(len(s))):
            min_char = min(min_char, s[i])
            min_suffix[i] = min_char

        stack = []
        result = []

        for i, char in enumerate(s):
            stack.append(char)
            count[char] -= 1

            # While the top of the stack is <= the smallest character left in s, pop from t to result
            while stack and (i == len(s) - 1 or stack[-1] <= min_suffix[i + 1]):
                result.append(stack.pop())

        return ''.join(result)