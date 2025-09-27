# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self._inorder(root)
        return self.res

    def _inorder(self,root):
        if not root:
            return
        self._inorder(root.left)
        self.res.append(root.val)
        self._inorder(root.right)

