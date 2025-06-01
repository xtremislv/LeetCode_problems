class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                # If neither top nor bottom has x at position i, it's impossible
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        # Try with tops[0] and bottoms[0] as potential targets
        rotations = min(check(tops[0]), check(bottoms[0]))
        return rotations if rotations != float('inf') else -1