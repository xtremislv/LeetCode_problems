from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        n = len(gain)
        altitudes = [0] * (n+1)
        for i in range(n):
            altitudes[i+1] = altitudes[i] + gain[i]
            max_altitude = max(max_altitude, altitudes[i+1])
        return max_altitude
        