class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
    
        # Generate the maximum possible number
        max_val = num
        for d in set(s):
            if d != '9':  # Try replacing digit d with '9'
                remapped = s.replace(d, '9')
                max_val = max(max_val, int(remapped))
    
        # Generate the minimum possible number
        min_val = num
        for d in set(s):
            if d != '0':  # Try replacing digit d with '0'
                remapped = s.replace(d, '0')
                min_val = min(min_val, int(remapped))
    
        return max_val - min_val