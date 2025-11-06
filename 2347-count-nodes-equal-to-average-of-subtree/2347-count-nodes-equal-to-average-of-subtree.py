# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0,0 #sum, num of nodes
            
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            s = ls + rs + node.val
            c = lc + rc + 1
            if node.val == s // c:
                self.res += 1
            return s, c
        dfs(root)
        return self.res
        

        
        



        