class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()  
        def backtrack(start, path):
            if len(path) >= 2:
                res.add(tuple(path))  
            
            used = set() 
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return [list(seq) for seq in res]