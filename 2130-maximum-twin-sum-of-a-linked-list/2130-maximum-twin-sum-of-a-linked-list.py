# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        ans = 0
        p1 , p2 = 0 , len(arr)-1

        while p1 < p2:
            ans = max(ans , arr[p1] + arr[p2])
            p1 += 1
            p2 -= 1
        
        return ans