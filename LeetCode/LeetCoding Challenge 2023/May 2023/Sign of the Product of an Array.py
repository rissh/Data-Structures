
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        sign = 1
        for num in nums:
            if num < 0:
                sign*= -1
        return sign
    
    
