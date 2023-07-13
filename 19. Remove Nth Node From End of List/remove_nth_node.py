# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        right, left = head, head
        distance = 1
        while distance <= n:
            right = right.next
            distance = distance + 1

        before_left = None
        while right:
            right = right.next
            before_left = left
            left = left.next

        if before_left:
            before_left.next = left.next
            return head
        else:
            return head.next
