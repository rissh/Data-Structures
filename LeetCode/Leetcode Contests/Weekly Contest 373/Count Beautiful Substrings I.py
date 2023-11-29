
def f(vowels, consonants,k):
        return vowels == consonants and (vowels * consonants) % k == 0
    
def isVowel(char):
    return char.lower() in {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        count = 0

        for i in range(n):
            vowl, cons = 0, 0
            for j in range(i, n):
                Curr = s[j]
                if isVowel(Curr):
                    vowl += 1
                else:
                    cons += 1
                        
                if vowl == cons and (vowl * cons) % k == 0:
                    count += 1
                

        return count
    