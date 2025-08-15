class Solution:
    def dfs(self, node, isConnected, visited):
        visited[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visited[i]:
                self.dfs(i, isConnected, visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]* n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                provinces += 1
        return provinces