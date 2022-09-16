
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort()
        count = 0
        
        maxi = -1
        prevx = -1
        lastx = 10 ** 10
        
        for x,y in properties[::-1]:
            if x != lastx:
                lastx = x
                maxi = prevx
            prevx = max(y, prevx)
            if y < maxi:
                count += 1
                
        return count
      
