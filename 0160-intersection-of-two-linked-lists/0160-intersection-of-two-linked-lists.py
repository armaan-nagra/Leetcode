# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #loop through one of the linked lists and create a set containing all nodes?
        #then loop through other linked list and if you're at a node which is in set, return it

        node_set = set()
        curr_A = headA
        while curr_A:
            node_set.add(curr_A)
            curr_A = curr_A.next
        
        curr_B = headB

        while curr_B:
            if curr_B in node_set:
                return curr_B
            curr_B = curr_B.next

        
        return None

