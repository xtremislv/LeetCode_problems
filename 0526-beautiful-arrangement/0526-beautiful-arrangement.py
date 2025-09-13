class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, visitied):
            if pos > n:
                return 1
            ans = 0
            for i in range(1, n+1):
                if not visited[i] and (i% pos == 0 or pos % i == 0):
                    visited[i] = True
                    ans += backtrack(pos +1, visited)
                    visited[i] = False

            return ans

        visited = [False] * (n+1)
        return backtrack(1, visited)

        # TIme O(n!)
        # Space O(n)