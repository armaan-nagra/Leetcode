# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #check left and right height at each node and if the abs diff is > 1, return False
        self.valid = True
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            if abs(left-right) > 1:
                self.valid = False

            return 1 + max(left, right)
        
        dfs(root)

        return self.valid