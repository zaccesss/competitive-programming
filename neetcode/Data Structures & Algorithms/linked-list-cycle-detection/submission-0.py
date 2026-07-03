# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            # Processed slow pointer
            slow = slow.next

            # Processed fast pointer
            fast = fast.next.next

            # Returned cycle found
            if slow == fast:
                return True

        # Returned no cycle
        return False