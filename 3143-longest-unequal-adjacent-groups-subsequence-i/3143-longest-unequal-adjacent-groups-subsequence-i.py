class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words or not groups:
            return []
    
        result = [words[0]]
        prev_group = groups[0]
    
        for i in range(1, len(words)):
            if groups[i] != prev_group:
                result.append(words[i])
                prev_group = groups[i]
    
        return result