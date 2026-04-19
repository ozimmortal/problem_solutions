# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([(root , 0)])
        col = defaultdict(list)
        while queue:
            
            node , l = queue.popleft()
            
            col[l].append(node.val)

            if node.left:
                queue.append([node.left , l + 1])
            if node.right:
                queue.append([node.right , l + 1])
        
        res = []
        for k in sorted(col , reverse=True):
            res.append(col[k])
        return res