# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        nums.sort()
        dummy = ListNode()
        curr = dummy
        for n in nums:
            temp = ListNode(n)
            curr.next = temp
            curr =curr . next
        return dummy.next
            