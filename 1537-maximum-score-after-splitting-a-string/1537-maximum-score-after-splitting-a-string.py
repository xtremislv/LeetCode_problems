class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        n = len(s)

        # Count total number of 1's initially (for the right part)
        total_ones = s.count('1')
        left_zeros = 0
        right_ones = total_ones

        # Try all split points from index 1 to n-1
        for i in range(n - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            max_score = max(max_score, left_zeros + right_ones)

        return max_score