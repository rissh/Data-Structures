
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        after = [[0 for i in range(k+1)] for i in range(2)]
        curr = [[0 for i in range(k+1)] for i in range(2)]
                
        ind = n-1
        while(ind >= 0):
            for buy in range(2):
                for cap in range(1,k+1):
                    
                    if(buy):
                        profit = max(-prices[ind]+ after[0][cap] , 0 + after[1][cap])
                        
                    else:
                        profit = max(prices[ind] + after[1][cap-1], 0 + after[0][cap])
        
                    curr[buy][cap] = profit
            
            ind -= 1
            after = [x for x in curr]
        
        return after[1][k]
      
