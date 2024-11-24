
class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        if n < 10:
            return False

        stones = 10
        turn = True 

        while n >= stones:

            n -= stones
            stones -= 1
            turn = not turn

        return  not turn
        
