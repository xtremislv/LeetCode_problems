class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.sum = 0  # Store the sum of values of all strings go through this node.

class MapSum:  # 24 ms, faster than 97.01%
    def __init__(self):
        self.trieRoot = TrieNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        curr = self.trieRoot
        for c in key:
            curr = curr.child[c]
            curr.sum += diff
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.trieRoot
        for c in prefix:
            if c not in curr.child: return 0
            curr = curr.child[c]
        return curr.sum