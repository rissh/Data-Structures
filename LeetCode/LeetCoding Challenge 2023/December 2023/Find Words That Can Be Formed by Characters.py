
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        def good(word, chars):
            word_count = Counter(word)
            chars_count = Counter(chars)

            for c in word_count.keys():
                if word_count[c] > chars_count[c]:
                    return False
            
            return True

        for word in words:
            if good(word, chars):
                res += len(word)

        return res
      
