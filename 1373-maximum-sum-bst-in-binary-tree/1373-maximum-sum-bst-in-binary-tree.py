# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node: 
                return 0, True, float('inf'), float('-inf')
                            
            l_sum, l_isbst, l_min, l_max = dfs(node.left)
            r_sum, r_isbst, r_min, r_max = dfs(node.right)

            if l_isbst and r_isbst and l_max < node.val < r_min:
                curr = l_sum + r_sum + node.val
                res = max(res, curr)

                return (
                    curr,
                    True,
                    min(l_min, node.val),
                    max(r_max, node.val)
                )
            else:
                return 0, False, 0, 0
        
        dfs(root)
        return res
        
        
      
        