class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:      
        
        def bfsAB(treeA, treeB):
            heightA, r1, c1 = treeA
            heightB, r2, c2 = treeB

            q = deque()
            q.append((r1, c1, 0))
            visited = set()

            while q:
                r, c, steps = q.popleft()
                visited.add((r, c))

                for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0 or nr >= rows
                        or nc < 0 or nc >= cols
                        or (nr, nc) in visited
                        or forest[nr][nc] == 0
                    ):
                        continue
                    
                    if forest[nr][nc] == heightB:
                        return steps + 1
                    
                    visited.add((nr, nc))
                    q.append((nr, nc, steps+1))
            
            return -1


        rows = len(forest)
        cols = len(forest[0])
        
        # 1) sorting the trees from shortest to tallest
        trees = []
        for r in range(rows):
            for c in range(cols):
                if forest[r][c] > 1:
                    trees.append([forest[r][c], r, c])
        trees.sort()

        # 2) doing a bfs from one tree to the next, and getting the dist from tree to tree
        # This is basically just a bfs problem. The hard trick is figuring out that the bfs search must be repeated from tree_i to tree_i+1
        totalDist = 0
        if forest[0][0] != trees[0][0]:
            totalDist = bfsAB([1, 0, 0], trees[0])
        if totalDist == -1:
            return -1

        for iTree in range(len(trees)-1):
            dist = bfsAB(trees[iTree], trees[iTree+1])
            if dist == -1:
                return -1
            totalDist += dist
        
        return totalDist
        



