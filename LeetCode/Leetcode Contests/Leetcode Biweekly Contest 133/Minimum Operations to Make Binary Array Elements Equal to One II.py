
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        curr = 1
    
        for num in nums:
            if num != curr:
                res += 1
                curr = 1 - curr  
    
        return res
        
