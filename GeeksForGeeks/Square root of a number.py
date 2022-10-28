# Method 1
#User function Template for python3

import math
#Complete this function
class Solution:
    def floorSqrt(self, x):
        
        if(x == 0 or x == 1):
            return x
            
        i = 1
        res = 1
        while(res <= x):
            i += 1
            res = i * i
        return i - 1   
      
# Method 2
#User function Template for python3

import math
#Complete this function
class Solution:
    def floorSqrt(self, x):
        
        if(x == 0 or x == 1):
            return x
            
        low = 1
        high = x // 2
        while(low <= high):
            mid = (high+low) // 2
            if(mid * mid == x):
                return mid
            elif(mid * mid < x):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans 
