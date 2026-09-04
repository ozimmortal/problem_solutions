# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def dfs(left , right):
            if left == right:
                return None
            
            mid = (left + right) // 2
            tree = TreeNode(nums[mid])
            tree.left = dfs(left , mid)
            tree.right = dfs(mid + 1 , right)
            return tree
        
        return dfs(0, len(nums))