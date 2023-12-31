
class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        n = len(words)
        #hashMap = defaultdict(int) -> It will also works fine
        hashMap = collections.Counter()

        for w in words:
            for c in w:
                hashMap[c] += 1

        for c in hashMap:
            if hashMap[c] % n:
                return False

        return True
      
