
class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c = 1, 1, 2
        for _ in range(n-2):
            a, b, c = a + b, c, b + c + 2*a
        return c % (pow(10, 9) + 7) if n > 1 else b
        
