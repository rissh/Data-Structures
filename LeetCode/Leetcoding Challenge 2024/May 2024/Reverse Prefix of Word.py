
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        n = len(word)

        if ch not in word:
            return word

        ind = word.index(ch)
        return word[:ind+1][::-1] + word[ind + 1:]
        
