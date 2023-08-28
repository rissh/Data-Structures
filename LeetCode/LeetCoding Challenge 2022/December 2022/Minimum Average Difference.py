
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sumfront,sumback,n = sum(nums),0,len(nums)
        ind,ans = 0,float('inf')
        
        for i in range(n):
            sumback+=nums[i]
            sumfront-=nums[i]

            bavg = sumback//(i+1) 
            savg = sumfront//(n-i-1) if i!=n-1 else 0
            
            if ans>abs(bavg-savg):
                ans = abs(bavg-savg)
                ind = i
        return ind
        
