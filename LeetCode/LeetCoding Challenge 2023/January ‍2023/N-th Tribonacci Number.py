
class Solution:
    def tribonacci(self, n: int) -> int:

        prev1, prev2, prev3 = 1,1,0
        if n == 0:
            return prev3
        
        if n == 1:
            return prev2

        if n == 2:
            return prev1

        output = 0
        for i in range(3,n+1):
            output = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = output

        return output
        
