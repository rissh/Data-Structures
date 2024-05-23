

def f(nums):
    
    n = len(nums)
    for i in range(n - 1):
        
        if nums[i] % 2 == nums[i + 1] % 2:
            return False
            
    return True
    
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        n = len(nums)
        m = len(queries)
    
        if n == 1:
            return [True] * m
    
        preSum = [0] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + (1 if nums[i] % 2 == nums[i - 1] % 2 else 0)
    
        res = []
        for start, end in queries:
            if start == end:
                res.append(True)
            else:
                count = preSum[end] - preSum[start]
                res.append(count == 0)
    
        return res
        
        
