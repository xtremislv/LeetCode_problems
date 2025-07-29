class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result =[]
        path =[]
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        def partpal(idx):
            if idx == len(s):
                result.append(path[:])
            for i in range(idx, len(s)):
                if isPalindrome(s, idx, i):
                    path.append(s[idx:i+1])
                    partpal(i +1)
                    path.pop()
        partpal(0)
        return result