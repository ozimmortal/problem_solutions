# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head

        arr = []
        def dfs(node):
            if not node: return 

            arr.append(node.val)
            dfs(node.next)
        dfs(head)
        arr.sort()

        res = ListNode(arr[0])
        curr = res
        for v in arr[1:]:
            temp = ListNode(v)
            curr.next = temp
            curr = curr.next
        return res

            