class Solution(object):
    def totalHammingDistance(self, nums):
        return sum(b.count('1') * b.count('0') for b in zip(*map('{:032b}'.format, nums)))