
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = []

        for num in nums:
            num = num*num
            res.append(num)
            
        res.sort()
        return res
      
