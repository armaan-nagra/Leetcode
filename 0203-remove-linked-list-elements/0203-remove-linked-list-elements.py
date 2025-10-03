# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #doesn't remove them from the start? in that case start off with dummy node?
        dummy = ListNode(val=0, next=head)
        curr = dummy
        #how do you fix it when there's multiple same values?
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            
            curr = curr.next
            
        return dummy.next
