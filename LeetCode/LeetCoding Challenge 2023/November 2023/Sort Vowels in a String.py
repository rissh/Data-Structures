
class Solution:
    def sortVowels(self, s: str) -> str:

        n = len(s)
        cons = collections.deque()
        vows = []

        for c in s:
            if c.lower() in "aeiou":
                vows.append(c)

            else:
                cons.append(c)

        
        vows.sort()
        vows = collections.deque(vows)
        res = []

        for c in s:
            if c.lower() in "aeiou":
                res.append(vows.popleft())

            else:
                res.append(cons.popleft())

        return "".join(res)
      
