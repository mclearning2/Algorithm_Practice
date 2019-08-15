# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:
    
    def serialize(self, root):
        # print("Serialize")
        # print(root)
        if not root:
            return []
            
        q = Queue()
        q.put(root)
        l = [root.val]
        
        while q.qsize():
            node = q.get()
            if node is None:
                continue
            
            q.put(node.left)
            q.put(node.right)
            
            l.append(None if node.left is None else node.left.val)
            l.append(None if node.right is None else node.right.val)
        
        
        index = -1
        while l[index] is None:
            index -= 1
        
        # print(l, index)
        return l[:index+1]
            
    def deserialize(self, data, index = 0):
        # print("Deserialize")
        # print(data)
        if data == []:
            return []
        
        root = TreeNode(data[0])
        
        q = Queue()
        q.put(root)
        l = [root.val]
        
        index = 0
        while index < len(data):
            
            node = q.get()
            # print(root)
            if node is None:
                continue
                
            index += 1
            if index >= len(data):
                break          
            
            if data[index] is not None:
                node.left = TreeNode(data[index])
                q.put(node.left)
            else:
                q.put(None)
                
            index += 1
            
            if index >= len(data):
                break
            
            if data[index] is not None:
                node.right = TreeNode(data[index])
                q.put(node.right)
            else:
                q.put(None)
            
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))