# definition for singly-linked list.
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

        # find the length of the linked list
        # also keep track of the tail node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # reduce unnecessary rotations
        # example:
        # length = 5, k = 7
        # rotating 7 times == rotating 2 times
        k = k % length

        # if k becomes 0 after modulo,
        # the list stays the same
        if k == 0:
            return head

        # connect the tail to the head
        # to make the list circular
        tail.next = head

        # find the new tail position
        # example:
        # length = 5, k = 2
        # new tail is at position 5 - 2 = 3
        steps = length - k

        new_tail = head

        # move to the new tail
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # the node after new_tail becomes new head
        new_head = new_tail.next

        # break the circular linked list
        new_tail.next = None

        # return the rotated list
        return new_head