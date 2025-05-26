from collections import deque, defaultdict
from typing import List
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # color_count[node][color] = max number of times color appears on any path ending at node
        color_count = [ [0]*26 for _ in range(n) ]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                color_count[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nei in graph[node]:
                for c in range(26):
                    curr = color_count[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0)
                    color_count[nei][c] = max(color_count[nei][c], curr)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

            max_color_value = max(max_color_value, max(color_count[node]))

        return max_color_value if visited == n else -1