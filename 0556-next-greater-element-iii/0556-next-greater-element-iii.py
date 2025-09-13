class Solution(object):
    def nextGreaterElement(self, n):
        digits = list(str(n))
        length = len(digits)
        pivot = -1

        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break

        digits[pivot + 1:] = digits[pivot + 1:][::-1]
        result = int(''.join(digits))

        return result if result <= 2**31 - 1 else -1