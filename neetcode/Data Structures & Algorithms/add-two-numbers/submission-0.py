class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node for the result list
        dummy = ListNode()
        cur = dummy
        carry = 0

        # Process both lists and any remaining carry
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            # Add the current digit
            cur.next = ListNode(total % 10)
            cur = cur.next

            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next