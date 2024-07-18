
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count, res = 1, 0
        start, end = head, head.next

        while end:

            if end.val == 0:
                end.val = res
                start = end
                end = end.next
                res = 0

            else:
                res += end.val
                end = end.next
                start.next = start.next.next
                
        return head.next
        
