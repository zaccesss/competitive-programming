# definition for singly-linked list.
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

        # used dummy to simplify list construction.
        dummy = ListNode()

        # used current to build merged list.
        current = dummy

        # processed both lists while nodes remained.
        while list1 and list2:

            # added node from list1 if smaller.
            if list1.val <= list2.val:

                current.next = list1
                list1 = list1.next

            # added node from list2 otherwise.
            else:

                current.next = list2
                list2 = list2.next

            # moved current pointer forward.
            current = current.next

        # connected remaining nodes from list1.
        if list1:
            current.next = list1

        # connected remaining nodes from list2.
        if list2:
            current.next = list2

        # returned merged list head.
        return dummy.next