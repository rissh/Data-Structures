
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        n = len(nums)
        visit = set()
        res = 0
    
        for num in nums:
            if num in visit:
                res ^= num
                
            else:
                visit.add(num)
    
        return res
      
