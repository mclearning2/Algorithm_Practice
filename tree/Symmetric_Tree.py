# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q_left = Queue()
        q_right = Queue()
        
        q_left.put(root)
        q_right.put(root)
        
        while True:
            l = q_left.get()
            r = q_right.get()            
            
            if l is None and r is None:
                if q_left.qsize() > 0 and q_right.qsize() > 0:
                    continue
                elif q_left.qsize() == 0 and q_right.qsize() == 0:
                    return True
                else:
                    return False                
            elif l is None or r is None:
                return False
            elif l.val != r.val:
                return False
            
            q_left.put(l.left)
            q_left.put(l.right)
            
            q_right.put(r.right)
            q_right.put(r.left)
        