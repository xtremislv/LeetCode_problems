class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(ransomNote)
        b = list(magazine)
        for x in a:
            if x in b:
                b.remove(x)
            else:
                return False
        return True
        