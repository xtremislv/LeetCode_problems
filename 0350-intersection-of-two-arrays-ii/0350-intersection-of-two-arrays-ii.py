class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        ar1 = Counter(nums1)
        ar2 = Counter(nums2)
        for i, j in ar1.items():
            if i in ar2:
                fre = min(j, ar2[i])
                for _ in range(fre):
                    out.append(i)
        return out