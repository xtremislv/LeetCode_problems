class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        visited = set()
        if not p:
            if not s:
                return True
            return False
        res = [0]
        self.dfs(s, p, 0, 0, visited, res)
        return res[0] == 1
    def dfs(self, s, p, si, pi, visited, res):
        if res[0]:
            return
        if (si, pi) in visited:
            return
        if not s[si:]:
            if not p[pi:]:
                res[0]=1
            if '*' in p[pi] and p[pi:].replace('*','') == '':
                res[0] = 1
            visited.add((si,pi))
            return
        if si == len(s)-1 and pi == len(p)-1:
            if p[pi] in ['?','*'] or s[si] == p[pi]:
                res[0] = 1
            visited.add((si,pi))
            return
        if p[pi] == '?':
            if si+1 <= len(s) and pi+1 < len(p):
                self.dfs(s, p, si +1, pi+1, visited, res)
        elif p[pi]=='*':
            if pi+1 < len(p):
                self.dfs(s, p, si, pi+1, visited, res)
            non_star = p[pi:].replace('*','')
            if len(s) - (si+1) >= len(non_star):
                self.dfs(s, p, si+1, pi, visited, res)
        else:
            if s[si] == p[pi]:
                if si+1 <= len(s) and pi+1 < len(p):
                    self.dfs(s, p, si+1, pi+1, visited, res)
        visited.add((si, pi))