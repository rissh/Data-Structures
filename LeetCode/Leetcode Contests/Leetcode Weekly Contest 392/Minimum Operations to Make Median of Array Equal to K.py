
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        medianInd = (n - 1) // 2 if n % 2 != 0 else n // 2
        res = 0
        
        for i, num in enumerate(nums):
            
            if num < k and i >= medianInd:
                res += k - num
                
            elif num > k and i <= medianInd:
                res += num - k
                
        return res
