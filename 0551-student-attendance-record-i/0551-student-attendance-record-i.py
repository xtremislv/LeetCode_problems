class Solution:
    def checkRecord(self, s: str) -> bool:
        i = 0
        for j in range(len(s)):
            if s[j] == 'A':
                i += 1
            if i == 2:
                break
        return i < 2 and s.find("LLL") < 0