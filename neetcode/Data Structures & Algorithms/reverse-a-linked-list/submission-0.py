# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        # Used prev to store the previous node.
        prev = None

        # Used curr to traverse the linked list.
        curr = head

        # Looped through the list until curr became None.
        while curr:

            # Saved the next node before reversing pointers.
            nextNode = curr.next

            # Reversed the current node pointer.
            curr.next = prev

            # Moved prev one step forward.
            prev = curr

            # Moved curr to the next node.
            curr = nextNode

        # Returned prev as the new head of the reversed list.
        return prev