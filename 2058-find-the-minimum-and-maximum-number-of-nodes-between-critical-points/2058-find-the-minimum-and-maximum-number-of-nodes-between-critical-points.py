# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        ans = [-1 , -1]
        far , near = 0 , 0
        idx, prev, curr = 2, head, head.next
        while curr and curr.next:
            nex = curr.next
            if prev.val < curr.val > nex.val or prev.val > curr.val < nex.val:
                if far != 0:
                    ans[-1] = max(ans[-1] , idx - far)
                if near != 0:
                    ans[0] = min(ans[0] , idx - near) if ans[0] != -1 else idx - near
                far = idx if far == 0 else far
                near = idx 
                
            prev = curr
            curr = nex
            idx += 1
        
        return ans