# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head != None:
            values.append(head.val)
            head = head.next
        
        values.sort()
        
        dummy = ListNode()
        copy = dummy 

        for x in range(len(values)):
            temp = ListNode(val=values[x])

            copy.next = temp
            copy = copy.next
        
        return dummy.next
        
            
