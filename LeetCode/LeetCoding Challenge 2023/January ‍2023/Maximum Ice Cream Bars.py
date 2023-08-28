
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        n = len(costs)
        count = 0

        if(min(costs) > coins):
            return 0

        costs.sort()

        for cost in costs:
            if cost  <= coins:
                count += 1
                coins -= cost
                
        return count
        
