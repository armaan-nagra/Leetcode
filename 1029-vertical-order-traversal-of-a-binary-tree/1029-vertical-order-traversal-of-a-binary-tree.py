# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use bfs?

        q = deque()
        q.append([root, 0, 0]) #store row and col
        column_map = defaultdict(list)

        while q:
            
            qLen = len(q)
            for x in range(qLen):
                node, row, col = q.popleft()
                column_map[col].append([row, node.val])
                if node.left:
                    q.append([node.left, row + 1, col - 1])
                if node.right:
                    q.append([node.right, row + 1, col + 1])

        res = []
        for col in sorted(column_map.keys()):
            column_map[col].sort(key=lambda x: (x[0], x[1]))
            res.append([val for _, val in column_map[col]])
        return res

