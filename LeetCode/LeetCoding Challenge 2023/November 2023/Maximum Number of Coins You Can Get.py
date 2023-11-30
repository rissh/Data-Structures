
class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles)
        res = 0

        piles.sort()
        #print(piles)
        i = n //3
        #print(i)
        while(i < n):
            res += piles[i]
            #print(piles[i])
            i += 2

        return res
      
