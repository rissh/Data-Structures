
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        n = len(happiness)
        happiness.sort(reverse=True)
        counter = 0
        res = 0
        
        for i in range(len(happiness)):
            res += max(0, happiness[i] - counter)
            counter += 1
            
            if counter >= k:
                break
                
        return res
        
