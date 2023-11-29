
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        n = len(words)
        nums = []
        
        for ind, word in enumerate(words):
            if x in word:
                nums.append(ind)
        
        return nums
        