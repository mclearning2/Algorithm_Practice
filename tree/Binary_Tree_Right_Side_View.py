# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answer = [root.val] if root else []
        def dfs(node, layer=0):
            if node is None:
                return
            
            if len(answer) -1 < layer:
                answer.append(node.val)
            
            dfs(node.right, layer + 1)
            dfs(node.left, layer + 1)            
            
        dfs(root)
            
        return answer