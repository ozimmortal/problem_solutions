# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        
        cidx = 1
        start , end = head , head

        for _ in range(right - left):
            end = end.next

        while cidx < left:
            start = start.next
            end = end.next
            cidx += 1

        temp = ListNode(start.val,end.next)

        while start != end:
            start = start.next
            temp = ListNode(start.val,temp)
           
        
        dummy = ListNode(0 , head)
        idx = 1
        prev = dummy
        while idx < left:
            idx += 1
            prev = prev.next

        prev.next = temp

        head =  dummy.next
        return head
        



        