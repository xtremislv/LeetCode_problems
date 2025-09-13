class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def d(a, b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        pts=[p1,p2,p3,p4]
        ds=[d(pts[i],pts[j]) for i in range(4) for j in range(i+1,4)]
        ds.sort()
        return ds[0]>0 and ds[0]==ds[1]==ds[2]==ds[3] and ds[4]==ds[5] and 2*ds[0]==ds[4]