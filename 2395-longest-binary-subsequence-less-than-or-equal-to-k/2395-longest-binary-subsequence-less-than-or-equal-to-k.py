class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        val = 0
        power = 1

        # Count trailing digits (right to left) that can be included without exceeding k
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if power <= k and val + power <= k:
                    val += power
                    count += 1
                else:
                    continue
            power <<= 1  # power *= 2

            # Optimization: if power exceeds k, no point in checking further as value will exceed
            if power > k:
                break

        # Count all '0's before the break point
        for j in range(i - 1, -1, -1):
            if s[j] == '0':
                count += 1

        return count