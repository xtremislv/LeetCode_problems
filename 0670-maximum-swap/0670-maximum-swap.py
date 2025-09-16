class Solution:
    def maximumSwap(self, num: int) -> int:
        s =[int(i) for i in str(num)]
        snew = sorted(s,reverse = True)
        d = defaultdict(int)
        n = len(s)
        for i in range(n):
            d[s[i]]=i
        for i in range(n):
            if s[i]!=snew[i]:
                s[i],s[d[snew[i]]] = s[d[snew[i]]],s[i]
                break
        ans = 0
        for i in s:
            ans+=i
            ans*=10
        return ans//10
        