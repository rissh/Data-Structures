
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = []
        curr = head
    
        while curr:
            nums.append(curr.val)
            curr = curr.next
    
        carry = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            new_val = nums[i] * 2 + carry
            carry, nums[i] = divmod(new_val, 10)
    
        if carry:
            nums.insert(0, carry)
    
        temp = ListNode()
        current = temp
        for num in nums:
            current.next = ListNode(num)
            current = current.next
    
        return temp.next
            
