
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        M = N-k
        total = sum(cardPoints)
        mn = s = sum(cardPoints[:M])
        
        for i in range(k):
            s -= cardPoints[i]
            s += cardPoints[i+M]
            mn = min(mn,s)
            
        return total - mn  
      
