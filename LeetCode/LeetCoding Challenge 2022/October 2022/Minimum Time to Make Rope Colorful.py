
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n = len(colors)
        i = j = 0
        res = 0
        
        while (i < n and j < n):
            maxTime = 0
            currTotal = 0
            
            while(j < n and colors[i] == colors[j]):
                maxTime = max(maxTime,neededTime[j])
                currTotal += neededTime[j]
                j += 1
                
            i = j
            res += (currTotal - maxTime)
        
        return res
      
