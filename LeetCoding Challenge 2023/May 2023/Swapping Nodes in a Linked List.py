
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        arr = []
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr[k-1],arr[-k] = arr[-k],arr[k-1]
        
        dummy = curr = ListNode(0)
        for a in arr:
            curr.next = ListNode(a)
            curr = curr.next
            
        return dummy.next
        
