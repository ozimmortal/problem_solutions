# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node , sub):            
            if not node and not sub :  return True

            if node and sub and node.val == sub.val:
                return sameTree(node.left,sub.left) and sameTree(node.right,sub.right)
            
            return False

        def dfs(n):
            if not n : return False

            if sameTree(n, subRoot): return True

            left = dfs(n.left)
            right = dfs(n.right)

            return left or right 
        
        return dfs(root) 