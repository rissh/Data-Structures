#
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = -1
        for i in nums:
            if i > res:
                if(-1 * i in nums):
                    res = i
        return res 
      
#
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        res = []
        for i in nums:
            if -1*i in nums:
                res.append(i)
        if res != []:
            return max(res)
        else: 
            return -1
