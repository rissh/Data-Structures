
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hashMap = dict(zip(heights,names))
        res = []
        heights.sort(reverse=True)
        
        for h in heights:
            res.append(hashMap[h])
            
        return res
      
