# definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        # used prev to store the previous node.
        prev = None

        # used curr to traverse the linked list.
        curr = head

        # looped through the list until curr became None.
        while curr:

            # saved the next node before reversing pointers.
            nextNode = curr.next

            # reversed the current node pointer.
            curr.next = prev

            # moved prev one step forward.
            prev = curr

            # moved curr to the next node.
            curr = nextNode

        # returned prev as the new head of the reversed list.
        return prev