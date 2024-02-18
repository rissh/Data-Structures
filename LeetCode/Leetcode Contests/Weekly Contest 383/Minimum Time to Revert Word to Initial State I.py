
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        n = len(word)
        
        for i in range(1, n // k + 1):
            if word[k * i:] == word[:n - k * i]:
                return i
        
        return n // k + 1

