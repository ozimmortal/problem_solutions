# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0 , head)
        prev = dummy

        slow , fast = head , head
        cn = 0

        while cn < n:
            fast = fast.next
            cn += 1
        
        while fast:
            slow = slow.next
            fast = fast.next
            prev = prev.next

        prev.next = slow.next
        
        return dummy.next

        

        