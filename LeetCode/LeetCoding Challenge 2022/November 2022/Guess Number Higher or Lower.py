
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                high = mid
            else:
                low = mid
        
        return low
      
