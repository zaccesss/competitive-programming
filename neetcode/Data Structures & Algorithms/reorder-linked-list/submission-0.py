class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge the two halves
        first, second = head, prev
        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2