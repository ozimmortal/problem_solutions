# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        c = {}
        for  i , n in enumerate(postorder):
            c[n] = i
        
        def dfs( i , j , k , l):

            if i > j or k > l:
                return
            
            node = TreeNode(preorder[i])
            if i != j:
                left = preorder[i + 1]
                mid = c[left]
                ls = mid - k + 1
                node.left = dfs(i + 1 , i + ls , k , mid)
                node.right= dfs(i + ls + 1 , j , mid + 1 , l -1)
            return node
        return dfs(0 , len(postorder) - 1 , 0, len(postorder) - 1)
