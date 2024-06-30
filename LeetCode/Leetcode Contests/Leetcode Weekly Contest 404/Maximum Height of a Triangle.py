

def f(redBalls, blueBalls):
    
    height = 0
    
    for i in range(1, max(redBalls, blueBalls) + 1):
        if i % 2 == 1:
            if redBalls >= i:
                redBalls -= i
            else:
                break
                
        else:
            if blueBalls >= i:
                blueBalls -= i
            else:
                break
                
        height += 1
    return height


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        
        return max(f(red, blue), f(blue, red))
        
