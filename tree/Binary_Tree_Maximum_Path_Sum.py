# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')
        
        def dfs(node):
            if node is None:
                return 0
            
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            
            self.max = max(self.max, l + r + node.val)
            return max(l, r) + node.val
        
        dfs(root)
        
        return self.max