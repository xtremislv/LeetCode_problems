# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack =[]
        fast = head
        l = 0
        while fast != None and fast.next!= None:
            l = l +2
            fast = fast.next.next
        temp = head
        i = 0
        maxi =- 1
        while temp != None:
            if i < l//2:
                stack.append(temp.val)
            elif stack:
                value = temp.val + stack.pop()
                maxi = max(maxi, value)
            
            i += 1
            temp = temp.next
        return maxi