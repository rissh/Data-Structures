

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack (num, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
                return 
                    
            for currNum in range(num+1, 10):
                if currNum <= target:
                    backtrack(currNum, stack+[currNum], target-currNum)
                    
                else:
                    return 
                      
        backtrack(0,[],n)
        
        return res
      



