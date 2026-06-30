# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dp(node):
            if not node:
                return [0 , 0]
            
            withLeft , withoutLeft = dp(node.left)
            withRight , withoutRight = dp(node.right)

            return [node.val + withoutLeft + withoutRight , 
                    max(withLeft , withoutLeft) + max(withRight , withoutRight)]
            
        
        return max(dp(root))