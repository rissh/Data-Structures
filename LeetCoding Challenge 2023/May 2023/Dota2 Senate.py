
class Solution:
    def predictPartyVictory(self, s: str) -> str:
        c = collections.Counter(s)

        def predict(s, r, d):
            if d == 0:
                return 'Radiant'
            if r== 0:
                return 'Dire'
            l = s[0]
            if l == 'R':
                ind = s.index('D')
                return predict(s[1:ind] + s[ind+1:] + s[0], r, d-1)
            if l == 'D':
                ind = s.index('R')
                return predict(s[1:ind] + s[ind+1:] + s[0], r-1, d)
                
        return predict(s, c['R'], c['D'])
        
