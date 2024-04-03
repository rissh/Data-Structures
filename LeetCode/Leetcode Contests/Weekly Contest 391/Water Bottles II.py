
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        total = numBottles
        remain = numBottles

        for i in range(remain // numExchange):
            exchanges = remain // numExchange
            
            if exchanges == 0:
                break
            else:
                total += 1
                remain = remain - numExchange + 1
                numExchange += 1
                
        return total
      
