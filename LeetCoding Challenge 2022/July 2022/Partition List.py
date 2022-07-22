
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a1 = b1 = ListNode(0)
        a2 = b2 = ListNode(0)
        
        while head:
            
            if head.val < x:
                b1.next = head
                b1 = b1.next
            else:
                b2.next = head
                b2 = b2.next
            head = head.next
            
        b2.next = None
        b1.next = a2.next
        return a1.next
        
