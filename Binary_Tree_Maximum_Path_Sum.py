# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, lower_bound=float('-inf'), upper_bound=float('inf')):
        if not root:
            return True

        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        
        return self.isValidBST(root.left, lower_bound, root.val) and \
               self.isValidBST(root.right, root.val, upper_bound)