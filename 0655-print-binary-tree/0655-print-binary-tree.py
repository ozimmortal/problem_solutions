# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left) , height(node.right))
        
        h = height(root)
        w = 2 ** h - 1

        tree = [[""] * w for _ in range(h)]
        queue = deque([(root , 0 , (w) //2)])

        while queue:
            node , r , c = queue.popleft()
            tree[r][c] = str(node.val)

            if node.left:
                nr , nc = r + 1 , c - 2**(h - r - 2)
                queue.append((node.left , nr ,nc))
            
            if node.right:
                nr , nc = r + 1 , c + 2**(h - r - 2)
                queue.append((node.right , nr ,nc))
        
        return tree




        

