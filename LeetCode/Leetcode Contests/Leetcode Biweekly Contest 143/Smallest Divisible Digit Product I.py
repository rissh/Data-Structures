
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        res = 0
        while True:
            product = 1
            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1
        
