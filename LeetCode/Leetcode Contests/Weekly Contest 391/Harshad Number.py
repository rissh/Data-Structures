
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        Sums = sum(int(i) for i in str(x))
        
        if x % Sums == 0:
            return Sums
        
        else:
            return -1
        
