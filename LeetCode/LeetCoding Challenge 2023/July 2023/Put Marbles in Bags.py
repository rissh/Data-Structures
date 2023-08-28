
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        n = len(weights)
        candidates = []
        
        
        for i in range(n-1):
            candidates.append(weights[i] + weights[i+1])
        
        
        candidates.sort()
        
        min_sum = 0
        max_sum = 0
        
        
        for i in range(k-1):
            min_sum += candidates[i]
            max_sum += candidates[n-2-i]
        
       
        return max_sum - min_sum
