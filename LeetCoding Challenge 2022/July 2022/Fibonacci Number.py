
def Fibonacci(n):
    if n==0:
        return 0
    prev = 1
    prev2 = 0
    i = 2
    while(i<=n):
        curr = prev + prev2
        prev2 = prev
        prev = curr
        i += 1
    return prev    
class Solution:
    def fib(self, n: int) -> int:
        return Fibonacci(n)
      
