
class Solution:
    def minOperations(self, s: str) -> int:

        # Two Pass Solution
        
        n = len(s)
        count1, count2 = 0,0

        for i in range(n):
            if i % 2 == 0 and s[i] != '0':
                count1 += 1
            elif i % 2 == 1 and s[i] != '1':
                count1 += 1

        for i in range(n):
            if i % 2 == 0 and s[i] != '1':
                count2 += 1
            elif i % 2 == 1 and s[i] != '0':
                count2 += 1

        res = min(count1, count2)
        return res
