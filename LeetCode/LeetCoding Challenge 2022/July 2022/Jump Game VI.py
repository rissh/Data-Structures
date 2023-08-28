
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        h = [(-nums[0],0)]
        
        for i in range(1,n):
            while(h[0][1]<i-k):
                heappop(h)
            maxi = h[0][0]
            heappush(h,(maxi-nums[i],i))
            if(i == n-1):
                return -(maxi-nums[i])
            
        return nums[0]       
      
