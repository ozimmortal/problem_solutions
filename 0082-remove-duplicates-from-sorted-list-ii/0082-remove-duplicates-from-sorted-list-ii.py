# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head
        dummy = ListNode(0)
        dummy_curr = dummy
        prev_val = -101
        while curr:
            
            while curr.next and curr.val == curr.next.val:
                prev_val = curr.val
                curr = curr.next
                
            if curr.val != prev_val:
                dummy_curr.next = ListNode(curr.val)
                dummy_curr = dummy_curr.next
    

            
            
            prev_val = curr.val
            curr = curr.next
            

        return dummy.next