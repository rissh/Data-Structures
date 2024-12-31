
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        res = []
        n = len(prices)

        for ind, p1 in enumerate(prices):
            for ind2 in range(ind +1, n):
                p2 = prices[ind2]

                if p2 <= p1:
                    res.append(p1 - p2)
                    break

            else:
                res.append(p1)
        
        return res
        
