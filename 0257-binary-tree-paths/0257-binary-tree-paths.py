# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        res = []
        def backtrack(node , path):
            
            if not node:
                return
            if node and not node.left and not node.right:
                path.append(str(node.val))
                s = "->".join(path)
                res.append(s)
                path.pop()
                return
            
            path.append(str(node.val))
            backtrack(node.left, path)
            backtrack(node.right, path)
            path.pop()



        backtrack(root , [])
        return res
