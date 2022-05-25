
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        env = sorted(envelopes, key=lambda x:(x[0],-x[1]))
        res = []
        
        for w,h in env:
            i = bisect_left(res,h)
            if i == len(res):
                res.append(h)
            else:
                res[i] = h
        return len(res)
      
