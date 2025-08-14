class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s1 = s
        s2 = s[::-1]
        @cache
        def evaluate(index1, index2):
            if (index1 < 0 or index2 < 0):
                return 0
            if (s1[index1] == s2[index2]):
                return 1 + evaluate(index1 -1, index2 -1)
            else:
                return max(evaluate(index1-1, index2), evaluate(index1, index2 -1))
        return n - evaluate(len(s1) -1, len(s2) - 1)