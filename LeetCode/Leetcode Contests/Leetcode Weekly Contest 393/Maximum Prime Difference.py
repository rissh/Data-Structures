

def f(n):
    
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        primes = [i for i, num in enumerate(nums) if f(num)] 
        
        if len(primes) < 2:
            return 0
        
        res = abs(primes[0] - primes[-1])
        return res
      
