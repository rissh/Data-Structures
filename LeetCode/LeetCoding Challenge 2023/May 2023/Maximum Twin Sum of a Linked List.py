
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        temp = head
        nums = []

        while temp:
            nums.append(temp.val)
            temp = temp.next

        res = 0
        n = len(nums)
        for i in range(n // 2):
            res = max(res, nums[i] + nums[n-1-i])

        return res
        
