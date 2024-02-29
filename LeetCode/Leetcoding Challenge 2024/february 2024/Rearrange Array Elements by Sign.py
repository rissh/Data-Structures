
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = [item for item in nums if item < 0]
        pos = [item for item in nums if item > 0]

        res = []
        n = len(nums) // 2

        for i in range(n):

            res.append(pos[i])
            res.append(neg[i])
            
        return res
      
