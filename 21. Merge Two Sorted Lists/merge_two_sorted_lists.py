# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        current = result

        while ((list1 is not None) and (list2 is not None)):
            current.next = ListNode()
            current = current.next
            if (list1.val < list2.val):
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

        while list1 is not None:
            current.next = ListNode()
            current = current.next
            current.val = list1.val
            list1 = list1.next

        while list2 is not None:
            current.next = ListNode()
            current = current.next
            current.val = list2.val
            list2 = list2.next

        return result.next
