
class Solution:
    def minOperations(self, k: int) -> int:

        res = float('inf')
        count = 0
    
        for i in range(1, k + 1):
            temp = count + k // i
            if k % i != 0:
                temp += 1
            res = min(res, temp)
            count += 1
        
        return res - 1
      
