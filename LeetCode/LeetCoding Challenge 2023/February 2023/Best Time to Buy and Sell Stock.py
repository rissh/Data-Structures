
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = prices[0]
        n = len(prices)
        
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit
    
        
        '''
        mini = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            cost = prices[i] - mini
            profit = max(profit,cost)
            mini = min(mini,prices[i])
        return profit
        '''
            
    
    '''
    sell, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < sell:
                sell = prices[i]
            profit = max(profit, prices[i]-sell)
        return profit
    '''
    
