class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j =0 
        for x in nums:
            if j <0:
                return False
            elif x > j:
                j = x
            j -= 1
        
        return True