class Solution(object):
    def constructArray(self, n, k):
        result = []
        left, right = 1, k + 1
        while left <= right:
            result.append(left)
            if left != right:
                result.append(right)
            left += 1
            right -= 1
        result.extend(range(k + 2, n + 1))
        return result