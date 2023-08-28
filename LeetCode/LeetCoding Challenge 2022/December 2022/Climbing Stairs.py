
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2,prev = 1,1
        i = 2
        while(i<=n):
            curr = prev + prev2
            prev2 = prev
            prev = curr
            i += 1
        return prev   
        
