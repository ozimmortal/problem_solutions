# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(n1 , n2):

            if not n1 and not n2:
                return
            
            Ll = ListNode()
            
            if n1 and n2:
                if n1.val < n2.val:
                    Ll.val = n1.val
                    Ll.next = dfs(n1.next , n2)
                else:
                    Ll.val = n2.val
                    Ll.next = dfs(n1 , n2.next)
            elif not n1 and n2:
                Ll.val = n2.val
                Ll.next = dfs(n1 , n2.next)
            elif not n2 and n1:
                Ll.val = n1.val
                Ll.next = dfs(n1.next , n2)

            return Ll
        return dfs(list1,list2)
