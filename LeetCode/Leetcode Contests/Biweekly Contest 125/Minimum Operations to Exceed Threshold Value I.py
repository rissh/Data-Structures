
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        res = 0
        
        while any(num < k for num in nums):
            target = min(nums)
            nums.remove(target)
            res += 1
            
        return res
      
