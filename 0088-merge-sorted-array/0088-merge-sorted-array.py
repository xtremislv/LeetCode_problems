class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = len(nums1)
        s = x - m
        while s > 0:
            nums1.pop()
            s = s-1 
        for q in nums2:
            nums1.append(q)
        nums1 = nums1.sort()
        