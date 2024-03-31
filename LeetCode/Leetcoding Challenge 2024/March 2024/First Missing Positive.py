
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        nums = set(nums)
        for i in range(1,2147483647):
            if i not in nums:      
                return i
              
