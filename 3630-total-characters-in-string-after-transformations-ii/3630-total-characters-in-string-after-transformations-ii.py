class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def mat_mult(A, B):
            # Multiply 26x26 matrices
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k] == 0:
                        continue
                    for j in range(26):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            # Raise matrix to power
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            while power:
                if power % 2 == 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result

        # Build the transformation matrix
        trans = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                trans[i][(i + k) % 26] += 1

        # Raise transformation matrix to the t-th power
        trans_t = mat_pow(trans, t)

        # Initial frequency vector
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Multiply initial vector with transformation matrix
        result = [0] * 26
        for i in range(26):
            for j in range(26):
                result[j] = (result[j] + freq[i] * trans_t[i][j]) % MOD

        return sum(result) % MOD
        