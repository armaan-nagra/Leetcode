# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #have like a queue, perform BFS and then insert in the root and height as a tuple
        if not root:
            return 0

        maxHeight = 0
        q = deque()
        q.append((root,1))

        while q:
            node, val = q.popleft()
            maxHeight = max(val, maxHeight)

            if node.left:
                q.append((node.left, val+1))
            if node.right:
                q.append((node.right, val+1))

        
        return maxHeight
