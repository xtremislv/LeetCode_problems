from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)
    
        # Build the tree
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 1: Compute time Bob reaches each node
        bob_time = [-1] * n
        def dfs_bob(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            for nei in graph[node]:
                if nei != parent and dfs_bob(nei, node, time + 1):
                    bob_time[node] = time
                    return True
            return False

        dfs_bob(bob, -1, 0)

        # Step 2: DFS for Alice
        def dfs_alice(node, parent, time):
            income = 0
            if bob_time[node] == -1 or time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2
            # Else Bob arrived earlier: income += 0

            max_child_income = -float('inf')
            is_leaf = True
            for nei in graph[node]:
                if nei != parent:
                    is_leaf = False
                    max_child_income = max(max_child_income, dfs_alice(nei, node, time + 1))
        
            return income if is_leaf else income + max_child_income

        return dfs_alice(0, -1, 0)