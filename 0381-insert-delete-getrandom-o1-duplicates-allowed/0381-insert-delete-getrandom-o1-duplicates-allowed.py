class RandomizedCollection:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        ans = val in self.map
        self.map.setdefault(val, set()).add(len(self.list))
        self.list.append(val)
        return not ans

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index_val = next(iter(self.map[val]))
        self.map[val].remove(index_val)
        if not self.map[val]:
            del self.map[val]
        if index_val != len(self.list) - 1:
            last_value = self.list[-1]
            self.map[last_value].remove(len(self.list) - 1)
            self.map[last_value].add(index_val)
            self.list[index_val] = last_value
        self.list.pop()
        return True

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.list) - 1)
        return self.list[ind]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()