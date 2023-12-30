
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        '''
        n = len(prices)
        prices.sort()
        
        sums = prices[0] + prices[1]
        
        res = money - sums
        if res >= 0:
            return res
        else:
            return money

        '''

        min1 = min2 = float("inf")

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p

        leftOver = money - min1 - min2

        return leftOver if leftOver >= 0 else money
      
