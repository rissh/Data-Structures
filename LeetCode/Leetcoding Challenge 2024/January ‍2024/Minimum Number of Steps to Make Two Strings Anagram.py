
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        n = len(s)
        def f(num):
            return collections.Counter(num)

        return sum((f(t) - f(s)).values())
        '''

        hashMap1 = [0] * 26
        hashMap2 = [0] * 26
        
        for num in s:
            hashMap1[ord(num) - ord('a')] += 1

        for num in t:
            hashMap2[ord(num) - ord('a')] += 1

        res = 0
        for i in range(26):
            res += abs(hashMap1[i] - hashMap2[i])

        return res // 2

