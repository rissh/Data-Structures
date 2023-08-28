
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        temp=sorted(nums)
        n=len(nums)
        i,j=0,len(nums)-1
        while i<n and nums[i]==temp[i]:
            i+=1 
        while j>=0 and nums[j]==temp[j]:
            j=j-1
        if j+1==0 and i==n:
            return 0
        return j-i+1
      
