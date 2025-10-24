# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('inf')
        #keep doing DFS and keep going down until you reach a node with no children, keep a res throughout

        while root:
            if abs(target - root.val) < abs(target - res) or (abs(target - root.val) == abs(target - res) and root.val < res):
                res = root.val

            if target > root.val:
                root = root.right
            elif target < root.val:
                root = root.left
            else:
                return root.val
            
        
        return res
            
        