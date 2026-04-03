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
        hashM = {}
        curr = head
        while curr:
            hashM[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                hashM[curr].next = hashM[curr.next]
            if curr.random:
                hashM[curr].random = hashM[curr.random]
            curr = curr.next
        return hashM[head]        