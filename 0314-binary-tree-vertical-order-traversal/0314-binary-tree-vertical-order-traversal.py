# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columns = defaultdict(list)

        #bfs? where when you add items to the queue, you also add in the column number

        q = deque()
        q.append((root, 0))
        columns[0].append(root.val)

        while q:


            for _ in range(len(q)):
                node, column = q.popleft()
                if node.left:
                    q.append((node.left, column - 1))
                    columns[column-1].append(node.left.val)
                if node.right:
                    q.append((node.right, column + 1))
                    columns[column+1].append(node.right.val)
        
        #convert this columns hash map into an array of arrays?
        column_indices = list(columns.keys())
        column_indices.sort()

        res = []
        for c in column_indices:
            res.append(columns[c])
        return res
