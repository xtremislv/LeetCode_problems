class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        # Calculate maximum tests per pig
        tests = minutesToTest // minutesToDie
        
        # Start with 0 pigs and increment until we have enough coverage
        pigs = 0
        while (tests + 1) ** pigs < buckets:
            pigs += 1
            
        return pigs