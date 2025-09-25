"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        nodes = {} 
        while curr:
            if curr not in nodes:
                nodes[curr] = Node(curr.val)
            curr = curr.next
        
        newCurr = head
        while newCurr:
            newNode = nodes[newCurr]
            newNode.next = nodes.get(newCurr.next)
            newNode.random = nodes.get(newCurr.random)

            newCurr = newCurr.next
        
        return nodes[head]
