class Solution:
    def get_prod_k(self, n, k):
        if n %k == 0:
            div = n//k
            return div**k
        else:
            rem = n%k
            div = (n-rem)//k
            power = k - rem
            prod = div ** (power)*((div+1)**rem)
        return prod
    def integerBreak(self, n: int) -> int:
        k_range = max(1+ n//2, 3)
        k_max = float('-inf')
        for k in range(2, k_range):
            cur_k = self.get_prod_k(n,k)
            k_max = max(k_max, cur_k)
        return k_max        