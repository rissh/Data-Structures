
class Solution:
    def minSwaps(self, s: str) -> int:

        n = len(s)
        close, maxClose = 0, 0

        for c in s:
            if c == Qop[;'
            f
            '] "[":
                close -= 1
            
            else:
                close += 1

            maxClose = max(maxClose, close)

        return (maxClose + 1) // 2

