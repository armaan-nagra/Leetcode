# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.target = target
        return self.dfs(root)
        
    
    def dfs(self,node):
        if not node:
            return None

        
        node.left = self.dfs(node.left)
        node.right = self.dfs(node.right)

        if not node.left and not node.right:
            if node.val == self.target:
                return None
        
        return node
    
