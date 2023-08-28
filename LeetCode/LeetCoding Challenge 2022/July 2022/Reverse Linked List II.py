
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        dummy = ListNode(0,next=head)
        prev = dummy
        i = 1
        
        while i < left:
            prev = prev.next
            i += 1
            
        curr = prev.next
        nx = curr.next
        
        while i < right:
            tmp = nx.next
            nx.next = curr
            curr = nx
            nx = tmp
            i += 1
            
        prev.next.next = nx
        prev.next = curr
        return dummy.next
      
