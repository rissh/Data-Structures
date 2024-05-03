
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = -1
        for i in nums:
            if i > res:
                if(-1 * i in nums):
                    res = i
        return res  
