# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        end = head
        pre = ListNode(next=head)
        new_head = pre
        should_reverse = True

        while True:
            if end is None:
                break
            for i in range(k-1):

                if (end.next is None):
                    should_reverse = False
                    break
                end = end.next
            if (should_reverse):

                post = end.next
                start = pre.next

                prev = start
                current = start.next
                while current != post:
                    temp = current.next
                    current.next = prev
                    prev = current
                    current = temp

                start.next = post
                pre.next = end

                end = post
                pre = start
            else:
                break

        return new_head.next
