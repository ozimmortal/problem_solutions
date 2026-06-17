# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def find_len(head):
            curr , length = head , 0
            while curr:
                curr = curr.next
                length +=1
            return length
        
        def reverse(head):
            if not head or not head.next :
                return head
            
            new_head= reverse(head.next)
            head.next.next = head
            head.next = None

            return new_head
            
            head.next = reve
        length = find_len(head)
        if length == 0:
            return head
            
        turn = k % length
        if turn == 0:
            return head

        for i in range(turn):
            head = reverse(head)
            head.next = reverse(head.next)
        
        return head
        


        
