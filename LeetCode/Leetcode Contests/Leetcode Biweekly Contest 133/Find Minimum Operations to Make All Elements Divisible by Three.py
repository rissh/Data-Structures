
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num % 3 == 1:
                count1 += 1
                
            elif num % 3 == 2:
                count2 += 1
                
        return count1 + count2
        
