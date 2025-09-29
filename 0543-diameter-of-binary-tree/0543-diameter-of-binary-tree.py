# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max = 0

        #returns height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            diameter = left + right

            self.max = max(self.max, diameter)

            return 1 + max(left, right) 


        dfs(root)
        return self.max


        
        
        

        
        