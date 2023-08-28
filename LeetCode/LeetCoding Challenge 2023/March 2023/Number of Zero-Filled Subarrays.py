
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        curr = 0
        
        if(nums.count(0) == 0):
            return 0
        
        for num in nums:
            if(num == 0):
                curr += 1
            else:
                res += ((curr) * (curr+1)) // 2
                curr = 0
                
        res += ((curr) * (curr+1)) // 2
        return res 
        
