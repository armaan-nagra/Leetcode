# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(TreeNode)
        def dfs(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        dfs(root)
        
        q = deque()
        q.append([target, 0])
        res = []
        visited = set()
        visited.add(target)
        while q:
            node, distance = q.popleft()

            if distance == k:
                res.append(node.val)
            if node.left and not node.left in visited:
                visited.add(node.left)
                q.append([node.left, distance + 1])

            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append([node.right, distance + 1])
            
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                q.append([parent[node], distance + 1])
        return res
            


