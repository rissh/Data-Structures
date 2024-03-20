
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        
        for num in nums:
            maxEle = max(map(int, str(num)))
            res += int(str(maxEle) * len(str(num)))
            
        return res
        
