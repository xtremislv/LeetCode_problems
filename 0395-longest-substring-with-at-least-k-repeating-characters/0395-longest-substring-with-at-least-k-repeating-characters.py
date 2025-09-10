class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return next((max(self.longestSubstring(t,k) for t in s.split(c)) for c in {*s} if s.count(c)<k), len(s))