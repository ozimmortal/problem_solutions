# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(head):
            if not head or not head.next : return 

            temp = head.val
            head.val = head.next.val
            head.next.val = temp

            swap(head.next.next)
        swap(head)
        return head


        