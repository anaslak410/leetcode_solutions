"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        obj_map = {}

        current = head
        new_head = Node(current.val)
        new_next = new_head
        obj_map[current] = new_head

        while current.next:
            new = new_next
            new_next = Node(current.next.val)
            new.next = new_next

            obj_map[current] = new
            current = current.next

        new = new_next
        obj_map[current] = new

        for key in obj_map:
            rand = key.random
            if rand in obj_map:
                obj_map[key].random = obj_map[rand]

        return new_head
