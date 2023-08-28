
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWordCompleted = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                newRoot.children[alphabetIndex] = TrieNode()
            newRoot = newRoot.children[alphabetIndex]
        newRoot.isWordCompleted = True
    
    def search(self, word: str) -> bool:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        if newRoot.isWordCompleted == True:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        newRoot = self.root
        for ch in prefix:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
