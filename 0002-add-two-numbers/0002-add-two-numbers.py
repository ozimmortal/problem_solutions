# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans , curr = None , None
        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry
            res = ListNode(s%10 ,None)
            carry = 1 if s >= 10 else 0

            if not ans:
                ans = res
                curr = ans
            else:
                curr.next = res
                curr = res
            
            l1 = l1.next
            l2 = l2.next

        # exhaust

        while l1:
            s = l1.val + carry
            res = ListNode(s%10 ,None)

            carry = 1 if s >= 10 else 0

            curr.next = res
            curr = res
            l1 = l1.next

        while l2:
            s = l2.val + carry
            res = ListNode(s%10 ,None)

            carry = 1 if s >= 10 else 0

            curr.next = res
            curr = res
            l2 = l2.next

        if carry == 1:
            res = ListNode(1,None)
            curr.next = res
            curr = res

        return ans

            
            

