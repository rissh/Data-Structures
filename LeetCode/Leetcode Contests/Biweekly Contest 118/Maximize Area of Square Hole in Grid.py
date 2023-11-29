
def f(arr):
    
    n = len(arr)
    Count, CurrCount = 0, 1
    
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 1:
            CurrCount += 1
        else:
            Count = max(Count, CurrCount + 1)
            CurrCount = 1
            
    Count = max(Count, CurrCount + 1)
    return Count

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        sort_H = sorted(hBars)
        sort_V = sorted(vBars)
        
        ans1 = f(sort_H)
        ans2 = f(sort_V)
        
        res = min(ans1, ans2)
        return res * res
    