
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
        res = 0
        direct = sum(abs(a - b) for a, b in zip(arr, brr))
    
        arr1 = sorted(arr)
        brr1 = sorted(brr)
        rearrange = sum(abs(a - b) for a, b in zip(arr1, brr1)) + k
    
        res = min(direct, rearrange)
        return res
        
