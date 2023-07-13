# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        will go with reverse approach
        """
        if head.next is None:
            return
        references = []

        current = head
        while current:
            references.append(current)
            current = current.next

        middle = (len(references) // 2) - 1
        current = len(references) - 1

        had = head
        while current > middle:
            temp = had.next
            had.next = references[current]
            had.next.next = temp
            had = temp
            current = current - 1

        if len(references) % 2 == 0:
            had.next = None
        else:
            had.next = references[middle+1]
            had.next.next = None
