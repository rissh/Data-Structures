# Method 1

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        hashMap = {}
        
        for i in range(n):
            hashMap[heights[i]] = names[i]
            
        heights.sort(reverse=True)
        ans = []
        
        for i in range(len(heights)):
            ans.append(hashMap[heights[i]])
            
        return ans

# Method 2
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hashMap = dict(zip(heights,names))
        res = []
        heights.sort(reverse=True)
        for h in heights:
            res.append(hashMap[h])
        return res
