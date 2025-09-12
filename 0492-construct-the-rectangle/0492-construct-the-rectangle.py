class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return next( [area//w, w] for w in range(int(area**0.5), 0, -1) if area % w == 0 )