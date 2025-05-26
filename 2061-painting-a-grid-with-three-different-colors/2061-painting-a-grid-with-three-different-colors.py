from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Generate all valid vertical colorings (no two adjacent cells have same color)
        def generate_states(m):
            states = []

            def dfs(pos, curr):
                if pos == m:
                    states.append(tuple(curr))
                    return
                for color in range(3):
                    if pos == 0 or curr[-1] != color:
                        curr.append(color)
                        dfs(pos + 1, curr)
                        curr.pop()

            dfs(0, [])
            return states

        # Check if two column states are compatible (no same color at any row)
        def is_compatible(a, b):
            for i in range(m):
                if a[i] == b[i]:
                    return False
            return True

        # Step 1: Generate all valid column states
        states = generate_states(m)
        state_count = len(states)

        # Step 2: Build adjacency graph of compatible states
        transitions = [[] for _ in range(state_count)]
        for i in range(state_count):
            for j in range(state_count):
                if is_compatible(states[i], states[j]):
                    transitions[i].append(j)

        # Step 3: DP: dp[col][state] = number of ways to color up to col ending with state
        dp = [1] * state_count  # Initial column (column 0)

        for _ in range(1, n):  # For each subsequent column
            new_dp = [0] * state_count
            for i in range(state_count):
                for j in transitions[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD
