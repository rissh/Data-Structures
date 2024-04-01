
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        res = float('inf')
        
        for i in range(n):
            Bit = 0
            for j in range(i, n):
                Bit |= nums[j]
                
                if Bit >= k:
                    res = min(res, j - i + 1)
                    break
                    
        return res if res != float('inf') else -1
      
