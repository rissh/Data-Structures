
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        
        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            res = max(res, diff)
    
        return res
        
