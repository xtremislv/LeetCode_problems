class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # Maximize a by changing the first non-9 digit to 9
        for ch in num_str:
            if ch != '9':
                a = int(num_str.replace(ch, '9'))
                break
        else:
            a = num  # Already all 9's
        
        # Minimize b
        if num_str[0] != '1':
            b = int(num_str.replace(num_str[0], '1'))
        else:
            for i in range(1, len(num_str)):
                if num_str[i] != '0' and num_str[i] != '1':
                    b = int(num_str.replace(num_str[i], '0'))
                    break
            else:
                b = num  # Nothing to change
        
        return a - b