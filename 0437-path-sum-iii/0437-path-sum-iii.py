# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        seen = Counter()
        seen[0] = 1
        count = 0
        def dfs(node , t):
            if not node: return 0
            nonlocal count
            
            t += node.val
            d = t - targetSum
            count += seen[d]
            seen[t] += 1

            left = dfs(node.left , t )
            right = dfs(node.right , t )

            seen[t] -= 1


        
        dfs(root,0)
        return count
            
  
            

            


        