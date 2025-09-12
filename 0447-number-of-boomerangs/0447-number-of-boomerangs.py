class Solution(object):
    def numberOfBoomerangs(self, points):
        from collections import defaultdict
        result = 0
        for p in points:
            distances = defaultdict(int)
            for q in points:
                d = (p[0] - q[0])**2 + (p[1] - q[1])**2
                distances[d] += 1
            for count in distances.values():
                result += count * (count - 1)
        return result