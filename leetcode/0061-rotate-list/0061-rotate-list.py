# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge cases:
        # - empty list
        # - only one node
        # - no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Find the length of the linked list
        # Also keep track of the tail node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        # Example:
        # length = 5, k = 7
        # rotating 7 times == rotating 2 times
        k = k % length

        # If k becomes 0 after modulo,
        # the list stays the same
        if k == 0:
            return head

        # Connect the tail to the head
        # to make the list circular
        tail.next = head

        # Find the new tail position
        # Example:
        # length = 5, k = 2
        # new tail is at position 5 - 2 = 3
        steps = length - k

        new_tail = head

        # Move to the new tail
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # The node after new_tail becomes new head
        new_head = new_tail.next

        # Break the circular linked list
        new_tail.next = None

        # Return the rotated list
        return new_head