# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        
        q = deque([root])
        res = []
        isre = False
        while q:
            n = len(q)
            temp = []
            for node in q:
                temp.append(node.val)

            res.append(temp[::-1] if isre else temp)
            isre = not isre

            for _ in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        return res
            
        