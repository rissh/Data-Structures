
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        n = len(word)
        hashMap = Counter(word)
        maxFreq = max(hashMap.values())
        res = float('inf')

        for i in range(1, maxFreq + 1):
            deletion = 0
            for freq in hashMap.values():
                if freq > i + k:
                    deletion += freq - (i + k)
                elif freq < i:
                    deletion += freq
            res = min(res, deletion)

        return res
