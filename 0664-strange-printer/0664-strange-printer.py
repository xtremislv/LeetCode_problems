class Solution:
    def strangePrinter(self, s: str) -> int:
        s = [c for c, _ in groupby(s)]
        s = [" "]+s
        n = len(s)

        @cache
        def cprint(i, j):
            if i < 0 or i > n or j < 0 or j > n:
                return 0
            if j <= i:
                return 0
            if j-i == 2:
                return 1
            if j-i < 2:
                return 0
            
            ans = 1 + cprint(i+1, j)
            for k in range(i+2, j):
                print(k, i+1)
                if s[k] == s[i+1]:
                    ans = min(ans, cprint(i, k) + cprint(k, j))

            return ans
        return cprint(0, n)