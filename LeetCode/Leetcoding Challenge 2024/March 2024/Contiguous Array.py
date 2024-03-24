
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        ps = 0
        prefix_sum_at_idx = {0: 0}
        for i, n in enumerate(nums):
            ps = ps+1 if n == 1 else ps-1
            
            if ps in prefix_sum_at_idx:
                res = max(res, i - prefix_sum_at_idx[ps] + 1)
            else:
                prefix_sum_at_idx[ps] = i+1
                
        return res
      
