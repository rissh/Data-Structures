
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def find(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        prev = head.val
        pre = temp
        temp = temp.next
    
        while temp is not None:
            curr = temp.val
        
            num = find(curr, prev)
            pre.next = ListNode(num)
            pre = pre.next
            pre.next = temp
            pre = temp
            temp = temp.next
            prev = curr
    
        return head
      
