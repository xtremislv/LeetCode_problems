class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        if k == 2:
            return [(p + q) / 2 for p,q in pairwise(nums)]
        kodd = k % 2
        ref = sorted(nums[:k])
        hl = [-x for x in ref[:k//2]]
        hl.reverse()
        hr = ref[k//2:]
        if kodd:
            out = [hr[0]]
        else:
            out = [(hr[0] - hl[0]) / 2]
        hrd = []
        hld = []
        def cleanr():
            while hrd and hrd[0] == hr[0]:
                heappop(hrd)
                heappop(hr)
        def cleanl():
            while hld and hld[0] == hl[0]:
                heappop(hld)
                heappop(hl)
        for idx,x in enumerate(nums[k:]):
            y = nums[idx]
            mid = hr[0]
            if y >= mid:
                if x < mid:
                    x = -heappushpop(hl, -x)
                    cleanl()
                heappush(hr, x)
                heappush(hrd, y)
                cleanr()
            else:
                if x >= mid:
                    x = heappushpop(hr, x)
                    cleanr()
                heappush(hl, -x)
                heappush(hld, -y)
                cleanl()
            if kodd:
                out.append(hr[0])
            else:
                out.append((hr[0] - hl[0]) / 2)
        return out