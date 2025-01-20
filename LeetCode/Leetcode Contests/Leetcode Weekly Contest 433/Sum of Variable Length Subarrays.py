
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
    
        for i in range(n):
            
            start = max(0, i - nums[i])
            currSum = sum(nums[start:i+1])
            
            res += currSum
    
        return res
        
