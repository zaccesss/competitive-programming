# definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # used slow and fast pointers for cycle detection.
        slow = head
        fast = head

        # processed the list until fast reached the end.
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # returned true if pointers met.
            if slow == fast:
                return True

        # returned false if no cycle exists.
        return False