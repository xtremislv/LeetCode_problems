class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        o=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s= sorted(d, key=lambda k:d[k], reverse=True)
        for i in range(k):
            o.append(s[i])
        return o
        