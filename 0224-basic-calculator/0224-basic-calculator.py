class Solution:
    def calculate(self, s: str) -> int:
        stack =[]
        num =0
        sign = 1
        ans = 0
        i = 0
        while(i<len(s)):
            ch = s[i]
            if ch.isdigit():
                num = int(ch)
                while i + 1 < len(s) and s[i+1].isdigit():
                    i+=1
                    num = num*10 + int(s[i])
                ans += sign*num
                num = 0
            elif ch=='+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif ch == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                ans = prev_result + prev_sign * ans
            i +=1
        return ans