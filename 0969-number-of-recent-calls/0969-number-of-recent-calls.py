from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = list()

    def ping(self, t: int) -> int:
        if t is None:
            return None
        else:
            self.q.append(t)
            srange = t - 3000
            erange = t
            count = 0
            for i in self.q:
                if i >= srange and i <= erange:
                    count += 1
            return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)