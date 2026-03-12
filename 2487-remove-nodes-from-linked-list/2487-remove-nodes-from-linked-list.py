# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [] # monotically decreasing stack

        curr = head

        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            
            stack.append(curr.val)
            curr = curr.next
        
        res, curr = None , None
        for e in stack:
            t = ListNode(e,None)

            if not res:
                res = t
                curr = t
            else:
                curr.next = t
                curr = t
        return res
        