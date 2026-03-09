# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd , even = None ,None
        idx = 1
        while head:
            if idx % 2 == 1:
                if not odd:
                    odd = ListNode(head.val,None)
                else:
                    temp = ListNode(head.val,None)
                    curr = odd
                    while curr.next:
                        curr = curr.next
                    curr.next = temp
            else:
                if not even:
                    even = ListNode(head.val,None)
                else:
                    temp = ListNode(head.val,None)
                    curr = even
                    while curr.next:
                        curr = curr.next
                    curr.next = temp
    
            head = head.next
            idx += 1
        
        curr = odd
        while curr and curr.next:
            curr = curr.next
        
        if curr:
            curr.next = even

        
        return odd

        
                
        
        