# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        sortedlist=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sortedlist.append(node.val)
            inorder(node.right)
        inorder(root)
        left=0
        right=len(sortedlist)-1
        while left<right:
            sum=sortedlist[left]+sortedlist[right]
            if sum<k:
                left+=1
            elif sum==k:
                return True
            else:
                right-=1
        return False