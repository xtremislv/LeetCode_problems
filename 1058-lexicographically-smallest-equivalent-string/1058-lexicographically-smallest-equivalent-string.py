class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]  # Each letter initially points to itself

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # Always keep the smaller lex character as the parent
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Union equivalent characters from s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Build the result using the smallest lexicographic equivalent
        result = []
        for ch in baseStr:
            smallest = find(ord(ch) - ord('a'))
            result.append(chr(smallest + ord('a')))

        return ''.join(result)