# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self._postOrder(root)
        return self.res


    def _postOrder(self,root):
        if not root:
            return 
        self._postOrder(root.left)
        self._postOrder(root.right)
        self.res.append(root.val)
