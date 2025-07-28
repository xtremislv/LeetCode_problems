class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        s =set(bank)
        if endGene not in s and startGene != endGene:
            return -1
        q =deque([(startGene, 0)])
        v ={startGene}
        while q :
            g, d = q.popleft()
            if g == endGene:
                return d
            for i in range(8):
                for c in 'ACGT':
                    if g[i] != c:
                        n = g[:i] + c + g[i+1:]
                        if n in s and n not in v:
                            v.add(n)
                            q.append((n, d+1))
        return -1