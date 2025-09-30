# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0     
        self.DFS(root, float('-inf'))
        return self.res

    def DFS(self, node, maxVal): #have to make sure that it's also bigger than previous and not just use max
        if not node:
            return
        if node.val >= maxVal:
            self.res += 1
        
        maxVal = max(maxVal, node.val)

        self.DFS(node.left, maxVal)
        self.DFS(node.right, maxVal)



        


            