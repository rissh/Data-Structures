
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low=0
        high=max(time)*totalTrips
        
        ans=0
        while low<=high:
            mid=(low+high)//2
            count=0
            for t in time:
                count=count+(mid//t)
            if count>=totalTrips:
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
        
        
