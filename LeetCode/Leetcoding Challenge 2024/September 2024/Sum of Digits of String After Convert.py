
class Solution:
    def getLucky(self, s: str, k: int) -> int:

        res = ''
        for x in s:
            res += str(ord(x) - ord('a') + 1)
        
        while k > 0:
            temp = 0
            for x in res:
                temp += int(x)  
            res = str(temp)  
            k -= 1

        return int(res)

