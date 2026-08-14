# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:


        def dfs(node, lt , s):
            if not node: return s - 1

            if lt:
                return max(dfs(node.left, False, s + 1) , dfs(node.right, True , 1))
            
            return max(dfs(node.right, True , s + 1) , dfs(node.left, False, 1 ))
        
        return max(dfs(root.left, False, 1) , dfs(root.right, True, 1)) 





        