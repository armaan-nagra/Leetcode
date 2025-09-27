# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self._preorder(root)
        return self.res

    def _preorder(self,root):
        if not root:
            return
        self.res.append(root.val)
        self._preorder(root.left)
        self._preorder(root.right)
