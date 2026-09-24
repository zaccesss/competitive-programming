# definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node handles the edge case where the head itself is the node to remove
        dummy = ListNode(0, head)
        first = head
        second = dummy

        # push first n nodes ahead so a fixed gap of n forms between first and second
        for _ in range(n):
            first = first.next

        # once first hits the end, second sits right before the target node,
        # since the gap between them stayed exactly n the whole way
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
