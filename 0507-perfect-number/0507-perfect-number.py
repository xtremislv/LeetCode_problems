class Solution:    
    def checkPerfectNumber(self,n):
        if n==1:
            return False
        sum=1
        for divisor in range(2,int(n**.5)+1):
            if n%divisor==0:
                if divisor==n//divisor:
                    sum+=divisor
                else:
                    sum+=divisor+(n//divisor)
        return n==sum