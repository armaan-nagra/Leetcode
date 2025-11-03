# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        self.nodeMap = {} #Node -> NodeCopy

        def dfs_first(node):
            if not node:
                return 
            self.nodeMap[node] = NodeCopy(val=node.val)
            dfs_first(node.left)
            dfs_first(node.right)
        
        dfs_first(root)
        
        #now do dfs again but add pointers etc...

        def dfs_second(node):
            if not node:
                return 
            
            copied_node = self.nodeMap[node]
            random = node.random
            if not random:
                copied_node.random = None
            else:
                copied_node.random = self.nodeMap[random]

            left = node.left
            if not left:
                copied_node.left = None    
            else:
                copied_node.left = self.nodeMap[left]

            right = node.right
            if not right:
                copied_node.right = None 
            else:
                copied_node.right = self.nodeMap[right]
            dfs_second(node.left)
            dfs_second(node.right)
        
        dfs_second(root)

        return self.nodeMap[root]

        