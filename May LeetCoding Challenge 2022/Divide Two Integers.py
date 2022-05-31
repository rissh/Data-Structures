
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=dividend/divisor
        if(res>=2**31):
            return (2**31)-1
        return int(res)
      
