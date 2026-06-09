# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def dfs(node):
            nonlocal ans

            if not node: return  0

            l = 1 + dfs(node.left)
            r = 1 + dfs(node.right)

            if abs(l - r) > 1:
                ans = False
                

            return max(l , r)
        dfs(root)

        return ans
        
        
            

