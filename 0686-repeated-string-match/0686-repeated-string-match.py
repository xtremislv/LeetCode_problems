import math

class Solution:
    def buildLPSLength(self, pattern):
        lps_length = [0] * len(pattern)
        length = 0
        j = 1
        
        while j < len(pattern):
            if pattern[j] == pattern[length]:
                length += 1
                lps_length[j] = length
                j += 1
            else:
                if length > 0:
                    length = lps_length[length - 1]
                else:
                    lps_length[j] = 0
                    j += 1
        
        return lps_length
    
    def kmp(self, text, pattern):
        lps_length = self.buildLPSLength(pattern)
        i = 0
        j = 0
        
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = lps_length[j - 1]
                else:
                    i += 1
            
            if j == len(pattern):
                return i - j
        
        return -1

    def repeatedStringMatch(self, a, b):
        a_repeated = a
        while len(a_repeated) < len(a) + len(b):
            a_repeated += a

        start_idx = self.kmp(a_repeated, b)
        if start_idx == -1:
            return -1

        return int(math.ceil(float(start_idx + len(b)) / len(a)))