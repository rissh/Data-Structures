
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        n = len(nums)
        res = []
    
        while nums:
            
            maxi = max(nums)
            nums.remove(maxi)
            
            mini = min(nums)
            nums.remove(mini)
            
        
            avg = (mini + maxi) / 2
            res.append(avg)
            
        ans = min(res)
    
        return float(format(ans, '.1f'))
    
