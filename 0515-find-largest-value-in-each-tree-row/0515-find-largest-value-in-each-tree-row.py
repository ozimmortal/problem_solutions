# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def findMax(nodes):
            maxi = float('-inf')

            for node in nodes:
                maxi = max(maxi,node.val)
            return maxi
        
        if not root: return []
        q = deque([root])
        res = []

        while q:
            n = len(q)
            res.append(findMax(q))
            for _ in range(n):
                node = q.popleft()
        
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res