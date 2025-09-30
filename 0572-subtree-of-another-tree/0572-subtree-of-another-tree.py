# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return (left or right)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True 
        if not p or not q:
            return False
        
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
