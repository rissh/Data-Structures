
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        w_set = set(words)
        @cache
        def dp(w:str) -> int:
            return 1 + max((dp(s) for i in range(len(w)) if (s:=w[:i]+w[i+1:]) in w_set), default=0)
        return max(dp(w) for w in words)
      
