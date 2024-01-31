
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        rep,mis = None,None
        res = Counter(nums)
        
        for i in range(1,n+1):
            if i not in res:
                mis = i
            if res[i] > 1:
                rep = i
                
        return [rep,mis]        
        
