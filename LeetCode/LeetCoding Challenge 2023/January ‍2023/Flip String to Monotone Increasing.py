
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        zeroes = s.count('0')
        once = 0
        res = zeroes

        for num in s:
            if num == '0':
                zeroes -= 1

            if num =='1':
                once += 1

            res = min(res,once+zeroes)

        return res
        
