
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num-1  not in nums:
                start = num
                while start in nums:
                    start += 1
                res = max(res,start-num)
        
        return res
      
