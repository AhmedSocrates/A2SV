# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        curr = before
        temp = after 
        
        ptr = head
        while ptr:
            if ptr.val<x:
                curr.next = ptr  
                curr = curr.next
            else:
                temp.next = ptr  
                temp = temp.next
            ptr = ptr.next

        temp.next = None
        curr.next = after.next
        return before.next
