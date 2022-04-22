
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        res = []
        
        for i in range(n):
            sums = 0
            for j in range(i,n):
                sums += nums[j]
                res.append(sums)
        res.sort()
        return sum(res[left-1:right])%1000000007
      
