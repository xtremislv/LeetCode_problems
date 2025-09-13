class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = [root]
        mxDepth = 0
        while q:
            mxDepth += 1
            nq = []
            for u in q:
                for v in u.children:
                    nq.append(v)
            q = nq
        return mxDepth