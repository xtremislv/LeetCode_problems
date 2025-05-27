class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
    
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # push next digit
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())  # pop to maintain order
    
        return ''.join(res)