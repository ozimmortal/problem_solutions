# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        counts = Counter()
        curr = headA
        while curr:
            counts[curr] += 1
            curr = curr.next
        
        curr = headB
        while curr:
            counts[curr] += 1
            curr = curr.next
        
        for key , freq in counts.items():
            if freq > 1:
                return key
        return 
        