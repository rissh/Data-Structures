
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head

        odd = curr = head
        even = evenhead = head.next
        i = 1

        while curr:
            if i > 2 and i % 2 != 0:
                odd.next = curr
                odd = odd.next

            elif i > 2 and i % 2 == 0:
                even.next = curr
                even = even.next

            curr = curr.next
            i += 1

        even.next = None
        odd.next = evenhead

        return head
        
