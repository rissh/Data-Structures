
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        cnt = 0

        for i in range(k):
            if s_list[i] in vowels:
                cnt = cnt + 1

        max_num = cnt

        for end in range(k,len(s)):
            start = end - k + 1
            if s_list[start-1] in vowels:
                cnt = cnt - 1
            if s_list[end] in vowels:
                cnt = cnt + 1
            max_num = max(max_num, cnt)
            
        return max_num        


        '''
        vowel = {'a', 'e', 'i', 'o', 'u'}
        left, count, res = 0,0,0
        n = len(s)

        for right in range(n):
            count += 1 if s[right] in vowel else 0

            if right - left + 1 > k:
                count -= 1 if s[left] in vowel else 0
                left += 1

            res = max(res,count)

        return res
        '''
        
