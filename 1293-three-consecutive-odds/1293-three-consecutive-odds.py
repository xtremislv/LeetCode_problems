class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        s =[]
        for x in range(len(arr) -2):
            q = arr[x]
            w = arr[x+1]
            e = arr[x+2]
            if q % 2 != 0 and w % 2 !=0 and e % 2 != 0:
                s.append(q)
                return True
        
        return False
        
        