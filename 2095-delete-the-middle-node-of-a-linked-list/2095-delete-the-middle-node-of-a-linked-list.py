# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0 , head)
        slow_ptr , fast_ptr = head , head
        behind = dummy

        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            behind = behind.next
        
        behind.next = slow_ptr.next if slow_ptr else None
        return dummy.next
        