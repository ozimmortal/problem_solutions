# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        store = defaultdict(TreeNode)
        childs = set()
        for p , c , left in descriptions:
            tp = TreeNode(p) if p not in store else store[p]
            tc = TreeNode(c) if c not in store else store[c]
            if left == 1:
                tp.left = tc
            else:
                tp.right = tc
            
            if p not in store:
                store[p] = tp
            if c not in store:
                store[c] = tc
            
            childs.add(c)
        
        for k in store:
            if k not in childs:
                return store[k]
        
         



        
        
