# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def solve(n , gp , p):
            if not n:
                return 0
            
            t = 0

            if gp and gp % 2 == 0:
                t += n.val

            t += solve(n.left , p , n.val)
            t += solve(n.right, p , n.val)

            return t

        return solve(root,None,None)
        