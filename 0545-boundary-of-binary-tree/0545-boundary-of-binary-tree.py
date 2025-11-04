# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = [root.val]
        
        #calculate left boundary, use DFS?
        self.left_boundary = []
        def dfsLeft(node):
            if not node:
                return 
            if not node.left and not node.right:
                return 
            self.left_boundary.append(node.val)
            
            if node.left:
                dfsLeft(node.left)
            else:
                dfsLeft(node.right)

        dfsLeft(root.left)
        res.extend(self.left_boundary)

        # #to calculate the leaves just use BFS
        # q = deque()
        # q.append(root)
        # leaves = []
        # while q:
        #     qLen = len(q)
        #     for x in range(qLen):
        #         node = q.popleft()
        #         if not node.left and not node.right:
        #             leaves.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # res.extend(leaves)
        # # prev contains the children
        leaves = []
        def addLeaves(node):
            if not node:
                return 
            if not node.left and not node.right:
                leaves.append(node.val)
                return 
            addLeaves(node.left)
            addLeaves(node.right)
        addLeaves(root)
        res.extend(leaves)



        self.right_boundary = []        
        def dfsRight(node):
            if not node:
                return 
            if not node.left and not node.right:
                return 
            self.right_boundary.append(node.val)

            if node.right:
                dfsRight(node.right)
            else:
                dfsRight(node.left)

        dfsRight(root.right)
        self.right_boundary.reverse()
        res.extend(self.right_boundary)

        return res

            

