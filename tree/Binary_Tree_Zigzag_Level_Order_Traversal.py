# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        
        def helper(node, layer=0):
            if node is None:
                return
            
            if len(answer) <= layer:
                answer.append([])
            
            if layer % 2:
                answer[layer].insert(0, node.val)
            else:
                answer[layer].append(node.val)
            
            helper(node.left, layer+1)
            helper(node.right, layer+1)
        
        helper(root)
        
        return answer