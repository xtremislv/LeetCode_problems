class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = list(haystack)
        b = list(needle)
        if needle in haystack:
            for x in range(len(a)):
                if needle == haystack[x:x+len(b)]:
                    return x  
        else:
            return -1
