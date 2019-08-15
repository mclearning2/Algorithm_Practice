# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        self.answer = None
        if not p or not q:
            return None
            
        def post_order(node):
            if node is None:
                return False
            
            left = post_order(node.left)
            right = post_order(node.right)
            
            if node.val == q.val or node.val == p.val:
                found = True
            else:
                found = False
            
            if (left and found) or (found and right) or (left and right):
                self.answer = node
            
            return left or right or found
        
        post_order(root)
        
        return self.answer