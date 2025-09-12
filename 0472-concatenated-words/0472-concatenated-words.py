class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)

        @functools.lru_cache
        def search(s):
            for i in range(1, len(s)):
                if s[:i] in words:
                    tail = s[i:]
                    if search(tail) or tail in words:
                        return True

            return False

        return [word for word in words if search(word)]

        