class Solution:

    def __init__(self, m: int, n: int):
        self.start = random.randint(0,m*n-1)
        self.m = m
        self.n = n
        
    def flip(self) -> List[int]:
        n1 = (self.start+1) % (self.m*self.n)
        self.start += 1
        return [n1 // self.n, n1 % self.n]
        

    def reset(self) -> None:
        self.start = random.randint(0,self.m*self.n-1)

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()