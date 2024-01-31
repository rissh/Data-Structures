
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])
        
        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))
        '''
        
        def f(s):
            return list(sorted(Counter(s).keys())), list(sorted(Counter(s).values()))

        return f(word1) == f(word2)
      
