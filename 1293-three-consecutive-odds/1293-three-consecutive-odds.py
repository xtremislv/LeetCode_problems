class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for s in range(len(arr)-2):
            if arr[s]%2 != 0 and arr[s+1]%2 != 0 and arr[s+2]%2!=0:
                return True
            
        return False