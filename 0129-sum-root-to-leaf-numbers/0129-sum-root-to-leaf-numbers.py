# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
    
        def dfs(node, number):
            if not node.left and not node.right:
                self.total += int(number + str(node.val))
            if node.left:
                dfs(node.left, number + str(node.val))
            if node.right:
                dfs(node.right, number + str(node.val))
        
        dfs(root, "")
        return self.total