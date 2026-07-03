# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Used dummy to simplify list construction.
        dummy = ListNode()

        # Used current to build merged list.
        current = dummy

        # Processed both lists while nodes remained.
        while list1 and list2:

            # Added node from list1 if smaller.
            if list1.val <= list2.val:

                current.next = list1
                list1 = list1.next

            # Added node from list2 otherwise.
            else:

                current.next = list2
                list2 = list2.next

            # Moved current pointer forward.
            current = current.next

        # Connected remaining nodes from list1.
        if list1:
            current.next = list1

        # Connected remaining nodes from list2.
        if list2:
            current.next = list2

        # Returned merged list head.
        return dummy.next