class Solution(object):
    def pacificAtlantic(self, heights):
        from collections import deque

        m = len(heights)
        n = len(heights[0])

        def f(s):
            v = set(s)
            q = deque(s)
            while q:
                r, c = q.popleft()
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    R, C = r + i, c + j
                    if 0 <= R < m and 0 <= C < n and (R, C) not in v and heights[R][C] >= heights[r][c]:
                        v.add((R, C))
                        q.append((R, C))
            return v

        p = [(x, 0) for x in range(m)] + [(0, x) for x in range(n)]
        a = [(x, n - 1) for x in range(m)] + [(m - 1, x) for x in range(n)]

        x = f(p)
        y = f(a)
        z = sorted(x & y)

        return [[r, c] for r, c in z]