"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #BFS, go through each item and in the queue, make the right element the next item in the queue      
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for x in range(n):
                node = q.popleft()
                if x == n - 1:
                    node.next = None
                else:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root

        