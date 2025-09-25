# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #add up nodes as you're going along l1 and l2, if at any point it's greater than 10, 
        #you mod it and add that to the new node and the div result is appended as a carry

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val
                toAdd = (value + carry) % 10
                carry = (value + carry) // 10

                curr.next = ListNode(val=toAdd)
                l1 = l1.next
                l2 = l2.next
                curr = curr.next
            elif l1:
                value = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10

                curr.next = ListNode(val=value)
                l1 = l1.next
                curr = curr.next
            elif l2:
                value = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10

                curr.next = ListNode(val=value)
                l2 = l2.next
                curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(val=carry)
        #not sure if the above is right, might need to loop until carry = 0

        return dummy.next





